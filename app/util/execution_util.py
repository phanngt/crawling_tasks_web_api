import traceback

from sqlalchemy.exc import SQLAlchemyError


def exec_safely(fn, *args):
    try:
        fn(*args)

    except SQLAlchemyError as exc:
        from app import db
        db.session.rollback()
        print('SQLAlchemy error:', exc)

    except Exception as ex:
        print('Error:', ex)
        traceback.print_exc()
