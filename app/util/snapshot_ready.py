from typing import List, Dict, Type
from .reflect import set_attribute_safely


class Snapshot(dict):
    def __init__(self, snapshot_id):
        super().__init__()
        self['__snapshot_id'] = snapshot_id

    def get_id(self):
        return self.get('__snapshot_id')


class SnapshotReady:
    SNAPSHOT_FIELDS: List[str] = []  # list[field_name]: to take snapshot
    LIST_ITEM_TYPES: Dict[str, Type] = {}  # dict[field_name, type]: to load list item in correct type from snapshot

    # dict[field_name, type]: to load nested object in correct type from snapshot.
    NESTED_OBJECT_TYPES: Dict[str, Type] = {}

    # noinspection PyMethodMayBeStatic
    def get_snapshot_id(self):
        """
        Overwrite this method to avoid infinity recursion when taking snapshot.

        :return: unique identity
        :rtype: str
        """
        return 'unique'

    def to_snapshot(self, stored_snapshots=None):
        """
        Take snapshot of fields in SNAPSHOT_FIELDS.

        :param stored_snapshots: dict[identity, snapshot]
        :type stored_snapshots: dict[str, Snapshot]
        :rtype: Snapshot
        """
        if stored_snapshots is None:
            stored_snapshots = dict()

        snapshot_id = self.get_snapshot_id()

        if snapshot_id in stored_snapshots:
            return stored_snapshots[snapshot_id]

        stored_snapshots[snapshot_id] = Snapshot(snapshot_id=snapshot_id)

        if not self.SNAPSHOT_FIELDS:
            return stored_snapshots[snapshot_id]

        for field in self.SNAPSHOT_FIELDS:
            if hasattr(self, field):
                stored_snapshots[snapshot_id][field] = get_snapshot(getattr(self, field), stored_snapshots)

        return stored_snapshots[snapshot_id]

    def from_snapshot(self, snapshot):
        """
        :type snapshot: Snapshot
        :rtype: SnapshotReady
        """
        if isinstance(snapshot, Snapshot):
            return load_from_snapshot(self, snapshot, {})

        return self


def get_snapshot(subject, stored_snapshots):
    """
    :type subject: Any
    :param stored_snapshots: dict[identity, snapshot]
    :type stored_snapshots: dict[str, Snapshot]
    """
    if isinstance(subject, SnapshotReady):
        return subject.to_snapshot(stored_snapshots)

    if isinstance(subject, list):
        return [item.to_snapshot(stored_snapshots) if isinstance(item, SnapshotReady) else item for item in subject]

    if isinstance(subject, dict):
        return {key: item.to_snapshot(stored_snapshots) if isinstance(item, SnapshotReady) else item
                for key, item in subject.items()}

    return subject


def load_from_snapshot(subject, snapshot, loaded_subjects):
    """
    :type subject: SnapshotReady
    :type snapshot: Snapshot
    :param loaded_subjects: dict[snapshot_id, subject]
    :type loaded_subjects: dict[str, SnapshotReady]
    :rtype: SnapshotReady
    """
    if snapshot.get_id() in loaded_subjects:
        return loaded_subjects[snapshot.get_id()]

    loaded_subjects[snapshot.get_id()] = subject

    for field, value in snapshot.items():
        if hasattr(subject, field):
            nested_object_type = getattr(subject, 'NESTED_OBJECT_TYPES', {}).get(field)
            if isinstance(nested_object_type, type) and issubclass(nested_object_type, SnapshotReady):
                if isinstance(value, Snapshot):
                    set_attribute_safely(subject, field,
                                         load_from_snapshot(nested_object_type(), value, loaded_subjects))
                # else: Skip
            else:
                list_item_type = getattr(subject, 'LIST_ITEM_TYPES', {}).get(field)
                if isinstance(list_item_type, type) and issubclass(list_item_type, SnapshotReady):
                    if isinstance(value, list):
                        set_attribute_safely(
                            subject, field,
                            [load_from_snapshot(list_item_type(), item, loaded_subjects)
                             for item in value if isinstance(item, Snapshot)])
                    # else: Skip
                else:
                    set_attribute_safely(subject, field, value)

    return subject
