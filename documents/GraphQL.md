*Note*:
+ Most of cases: Get all <=> itemsToGet: 200.
+ itemsToGet <= 200.
+ rangeLimit <= 1000.
+ Random: take first [rangeLimit] entries => take randomly [itemsToGet] entries from these entries.

1 Chart -> N Track:
```
query {
	chart(chartId: "47217A038CAC4EA69F0C5156F0A8BF49") {
    name
    description
    category
    displayOrder
    webUri
    genreId
    regionId
    playlistId
    tracks(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

1 Track -> N DataSource:
```
query {
  track(trackId: "73455FE485A84C8090AF7C9ADE0CE071") {
    id
    title
    artistName
    webUri
    dataSources(startPoint: 0, itemsToGet: 20) {
      id
      fileUrl
      durationMs
      width
      height
      isVideo
      playerAudioVolume
      displayAt
      formatId
      formatName
      priority
    }
  }
}
```

1 Album -> N UserNarrative:
```
{
  album(albumId: "CD4DE21C02A94861A23466F7FAD8B156") {
    id
    title
    squareImage {
      url
      mimeType
    }
    webUri
    nUserNarratives
    userNarratives(startPoint: 0, itemsToGet: 20) {
      importance
      publishedAt
      readMins
      authorId
      author {
        username
        fullName
        profilePictureUrl
      }
      tags {
        id
        title
      }
      sections {
        title
        datasource {
          durationMs
          fileUrl
          width
          height
          isVideo
          playerAudioVolume
          displayAt
          track {
            id
            title
            artistName
            coverImage {
              url
              mimeType
            }
            webUri
            artist {
              id
              name
              webUri
            }
            album {
              id
              squareImage {
                url
                width
                height
                mimeType
              }
              webUri
            }
          }
        }
        content
      }
      title
    }
  }
}
```

1 Playlist -> N Track:
```
{
	playlist(playlistId: "D64FACE6DD924835A8D84D2BE921A626") {
    title
    description
    webUri
    tracks(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

Classic/New -> N Track:
```
query {
  classicNew(genreIds: ["531291675631043", "49116767185384"], categories: ["new"]) {
    categories
    genreIds
    randomTracks(itemsToGet: 50, rangeLimit: 500) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

1 Theme -> N Track:
```
{
  theme(themeId: "196059980955404") {
    title
    description
    genreId
    tracksInAlbums(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

User page -> Track List:
```
{
  userProfile(username: "kaz_piro_piro") {
    id
    fullName
    profilePictureUrl
    nTracks
    tracks(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

Total numbers:
```
{
  playlist(playlistId: "D64FACE6DD924835A8D84D2BE921A626") {
    nTracks
  }
  chart(chartId: "47217A038CAC4EA69F0C5156F0A8BF49") {
    nTracks
  }  
  album(albumId: "8371B138EBC74670ABE3873FE0E5CEC0") {
    nTracks
  }
  userProfile(username: "kaz_piro_piro") {
    nTracks
  }
}
```

Approximated numbers:
```
query {
    roughNNarratedAlbums
}
```

Feature Albums with User Narrative:
```
{
  narratedAlbums(startPoint: 0, itemsToGet: 20, shuffled: true) {
    id
    title
    artist {
      id
      name
      squareImage {
        url
        width
        height
        mimeType
      }
      webUri
    }
    squareImage {
      url
      width
      height
      mimeType
    }
    webUri
    topUserNarrative {
      id
      title
      importance
      publishedAt
      readMins
      author {
        id
        username
        fullName
        profilePictureUrl
      }
      tags {
        id
        title
      }
      sections {
        title
        datasourceId
        content
      }
    }
  }
}
```

1 User - N Collected Items:
```
{
  userProfile(username: "camjameson") {
    id
    fullName
    profilePictureUrl
    nFollowers
    nFollowing
    nTracks
    nPlaylists
    nArtists
    nAlbums
    tracks(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
    playlists(startPoint: 0, itemsToGet: 20) {
      id
      title
      description
      owner {
        id
        username
        fullName
        profilePictureUrl
      }
      coverUrls
      webUri
    }
    artists(startPoint: 0, itemsToGet: 20) {
      id
      name
      squareImage {
        url
        width
        height
        mimeType
      }
      webUri
    }
    albums(startPoint: 0, itemsToGet: 20) {
      id
      title
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      squareImage {
        url
        width
        height
        mimeType
      }
      webUri
    }
  }
}
```

1 Artist - Various Tracks:
```
{
  artist(artistId: "758EB6EA11C4945098996712EE98E6AB") {
    id
    trackCount {
      trackList
      official
      audio
    }
    dataSourceCount {
      live
      featuringRemixes
      covers
      total
    }    
    tracks(officialOnly: true, startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
    officialTracks(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
    audioTracks(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }    
    liveTrackDataSources(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }    
    featureRemixTrackDataSources(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }    
    coverTrackDataSources(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }    
  }
}
```

1 Album - Various Tracks:
```
{
  album(albumId: "D347986E804E44B7ABF4B83F185450E5") {
    title
    squareImage {
      url
      width
      height
      mimeType
    }
    webUri
    trackStats {
      nTotal
      nOfficial
      nLive
      nFeatureRemix
    }
    tracks(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
    officialTracks(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
    liveTracks(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
    featureRemixTracks(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

Find by YouTube URL:
```
{
  findByYoutubeUrl(youtubeUrl:"https://www.youtube.com/watch?v=nfWlot6h_JM") {
    id
    title
    durationMs
    coverImage {
      url
      width
      height
      mimeType
    }
    datasourceId
    previewUrl
    playerAudioVolume
    url
    width
    height
    isVideo
    displayAt
    artistName
    webUri
    artist {
      id
      name
      webUri
      squareImage {
        url
        width
        height
        mimeType
      }
    }    
  }
}
```

Find by data source ID:
```
{
  dataSource(dataSourceId: "BCA173BB8DC34966B7456AD3B10CA895") {
    durationMs
    fileUrl
    width
    height
    isVideo
    playerAudioVolume
    displayAt
    track {
      id
      title
      artistName
      coverImage {
        url
        mimeType
      }
      webUri
      artist {
        id
        name
        webUri
      }
    }
  }
}
```

Sign in:
```
mutation {
  signIn(username: "longpV", password: "grqb1jNLuJp/0rxzIDol1ChopLnlcXmuzJEI3S/af8DlDefxvaKSIklIgaTUXo+y6kcTOjXt73CYd1kvB8/Y4mzU3m+924RQOoTRpWdTRKiZjKt1xzgoEgBxPcJ8s0JhEapl5lGARoTahZE9nfo2wTq69nv3vlACUsemTK5PJoxzcroTs8+Rq4999g+UtKkTqxjsXJ9FEX+9izPTJv0i69FjlEpEqcphT4CB5bUH+hst2ulQ/Uu81vORijIZkXJisv/xlJjjrmdCsJuQuAFlr9QauZq+9lFZi5YMmlrhf1HQiAYW3iLjZcA3Cc3miji+SuMlzotQMQJyIg0qFzf6Dg==", deviceId: "TestDevice8668") {
    token
    tokenExpiresAt
    user {
      id
      username
      email
    }
  }
}
```

Find user by username:
```
{
  userProfile(username: "kaz_piro_piro") {
    id
    username
    fullName
    profilePictureUrl
    socials {
      socialName
      identifier
      socialUrl
    }
  }
}
```

Find user by ID:
```
{
  userProfile(userId: "498273542225616") {
    id
    username
    fullName
    profilePictureUrl
    socials {
      socialName
      identifier
      socialUrl
    }
  }
}
```

Artist page -> Track List:
```
{
  artist(artistId: "427FFBFBD32394606BFDD9C92300B38C") {
    id
    name
    webUri
    squareImage {
      url
      width
      height
      mimeType
    }
    trackCount {
      trackList
      official
      audio
    }
    tracks(officialOnly: true, sortClause:"latest", startPoint: 0, itemsToGet: 12) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

Artist page -> Track List -> See All:
```
{
  artist(artistId: "427FFBFBD32394606BFDD9C92300B38C") {
    id
    name
    webUri
    squareImage {
      url
      width
      height
      mimeType
    }
    tracks(sortClause:"latest", startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

1 Album -> Track list, Official, Live, Featuring Remixes:
```
{
  album(albumId: "CD4DE21C02A94861A23466F7FAD8B156") {
    title
    squareImage {
      url
      width
      height
      mimeType
    }
    webUri
    trackCount {
      trackList
      official
    }
    dataSourceCount {
      live
      featuringRemixes
    }
    tracks(startPoint: 0, itemsToGet: 200) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
    officialTracks(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
    liveTrackDataSources(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
    featureRemixTrackDataSources(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

1 Track -> Official, Track List, Live, Featuring Remixes, Covers, Review, Lyrics, Single Info, Artist, Album:
```
{
  track(trackId: "FBC484D0A4C446208E0BA96560AEE737") {
    id
    title
    coverImage {
      url
      width
      height
      mimeType
    }
    previewUrl
    durationMs
    webUri
    dataSourceCount {
      trackList
      trackListNonOfficial
      official
      live
      featuringRemixes
      covers
    }
    officialDataSources {
      id
      title
      artistName
      fileUrl
      previewUrl
      durationMs
      width
      height
      isVideo
      playerAudioVolume
      displayAt
      formatId
      formatName
      priority
    }    
    trackListNonOfficialDataSources(startPoint: 0, itemsToGet: 20) {
      id
      title
      artistName
      fileUrl
      previewUrl
      durationMs
      width
      height
      isVideo
      playerAudioVolume
      displayAt
      formatId
      formatName
      priority
    }    
    liveDataSources(startPoint: 0, itemsToGet: 20) {
      id
      title
      artistName
      fileUrl
      previewUrl
      durationMs
      width
      height
      isVideo
      playerAudioVolume
      displayAt
      formatId
      formatName
      priority
    }    
    featureRemixDataSources(startPoint: 0, itemsToGet: 20) {
      id
      title
      artistName
      fileUrl
      previewUrl
      durationMs
      width
      height
      isVideo
      playerAudioVolume
      displayAt
      formatId
      formatName
      priority
    }    
    coverDataSources(startPoint: 0, itemsToGet: 20) {
      id
      title
      artistName
      fileUrl
      previewUrl
      durationMs
      width
      height
      isVideo
      playerAudioVolume
      displayAt
      formatId
      formatName
      priority
    }    
    recorded
    released
    lyrics
    review
    wikipediaUrl
    wikipediaBrief
    genres
    writers
    labels
    studios
    producers
    artist {
      id
      name
      squareImage {
        url
        width
        height
        mimeType
      }
      webUri
    }
    album {
      id
      title
      squareImage {
        url
        width
        height
        mimeType
      }
      webUri
    }
  }
}
```

Test TrackIDs: FBC484D0A4C446208E0BA96560AEE737 (Shallow), 260C5FA46C1042D3A359FD67AED471F0 (Make Me Like You), 7375302F968C4E198B8060301D4B71E8 (Thank U, Next).

User Playlist:
```
{
	playlist(playlistId: "D64FACE6DD924835A8D84D2BE921A626") {
    title
    description
    webUri
    nTracks
    tracks(sortClause: TIMESTAMP, startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

TOP 100 Playlist:
```
{
	playlist(playlistId: "D64FACE6DD924835A8D84D2BE921A626") {
    title
    description
    webUri
    nTracks    
    tracks(sortClause: PRIORITY, startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

Theme page -> Track List:
```
{
  theme(themeId: "196059980955404") {
    title
    description
    genreId
    trackCount {
      trackList
    }
    trackList(albumsToGet: 6, tracksPerAlbum: 2, areRandomTracks: true) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

Theme page -> Track List -> See All:
```
{
  theme(themeId: "196059980955404") {
    title
    description
    genreId
    trackCount {
      trackList
    }
    tracksInAlbums(startPoint: 0, itemsToGet: 20) {
      id
      title
      durationMs
      artistName
      coverImage {
        url
        width
        height
        mimeType
      }
      artist {
        id
        name
        squareImage {
          url
          width
          height
          mimeType
        }
        webUri
      }
      previewUrl
      webUri
      datasourceId
      url
      width
      height
      isVideo
      playerAudioVolume
      displayAt
    }
  }
}
```

Album -> Artist List:
```
{
  album(albumId: "49D93C7F50EE4F369602DF2A690A6FB7") {
    title
    nArtists
    artists(startPoint: 0, itemsToGet: 4) {
      id
      name
      squareImage {
        url
        width
        height
        mimeType
      }
      webUri
    }
  }
}
```
Note: Some albums have 2 artists or more.

Artist page -> Narrated Albums:
```
{
  artist(artistId: "758EB6EA11C4945098996712EE98E6AB") {
    id
    name
    webUri
    squareImage {
      url
      width
      height
      mimeType
    }
    nNarratedAlbums
    narratedAlbums(albumStartPoint: 0, albumsToGet: 3, shuffled: false) {
      id
      title
      squareImage {
        url
        width
        height
        mimeType
      }
      webUri
      topUserNarrative {
        id
        title
        importance
        publishedAt
        readMins
        author {
          id
          username
          fullName
          profilePictureUrl
        }
        tags {
          id
          title
        }
        sections {
          title
          datasourceId
          content
        }
      }
    }
  }
}
```

Note: use Album ID of first album to get 2 narratives:
```
{
  album(albumId: "113B41D315704F70B78AA5B3FC35FBF0") {
    id
    title
    squareImage {
      url
      mimeType
    }
    webUri
    colorPrimary
    colorText    
    userNarratives(startPoint: 0, itemsToGet: 2) {
      id
      title
      importance
      publishedAt
      readMins
      author {
        id
        username
        fullName
        profilePictureUrl
      }
      tags {
        id
        title
      }
      sections {
        title
        datasourceId
        content
      }
    }
  }
}
```

Artist page -> Album Narratives -> See All:
```
{
  artist(artistId: "758EB6EA11C4945098996712EE98E6AB") {
    id
    name
    webUri
    squareImage {
      url
      width
      height
      mimeType
    }
    nAlbumNarratives
    albumNarratives(startPoint: 0, itemsToGet: 20) {
      id
      title
      squareImage {
        url
        width
        height
        mimeType
      }
      webUri
      topUserNarrative {
        id
        title
        importance
        publishedAt
        readMins
        author {
          id
          username
          fullName
          profilePictureUrl
        }
        tags {
          id
          title
        }
        sections {
          title
          datasourceId
          content
        }
      }
    }
  }
}
```

Genre for Breadcrumb:
```
{
  track(trackId: "0000F8C199D94C079EB1E3CEC0B64AB1") {
    title
    webUri
    genreForBreadcrumb {
      title
      id
      chartId
    }
  }
  artist(artistId: "D837C95D662D411A9792A2CBFB6F00CC") {
    name
    webUri
    genreForBreadcrumb {
      title
      id
      chartId
    }
  }
  album(albumId: "F740A38E4C0345C5A5019166F2F80AA7") {
    title
    webUri
    genreForBreadcrumb {
      title
      id
      chartId
    }
  }
}

```

Chart -> Narrated Albums (by Genre):
```
{
  chart(chartId: "CC6AE7D721F742849FAFF24A5593D4FF") {
    id
    genreId
    name
    nNarratedAlbums
    narratedAlbums(startPoint: 0, itemsToGet: 20) {
      title
      webUri
      artist {
        name
        webUri
      }
      topUserNarrative {
        id
        title
        brief
        publishedAt
        tags {
          id
          title
        }
        author {
          username
          profilePictureUrl
        }
      }
    }
  }
}
```
Charts: ROCK (CC6AE7D721F742849FAFF24A5593D4FF), US 100 (47217A038CAC4EA69F0C5156F0A8BF49), WORLD (5FE8BD1991CA4676BA32A1A872EC59A5), POP (336B3E4A9D344CFE8B205726DC254748)

Optimized:
```
{
  playlist(playlistId:"632D2201807D46E29BAC1C730CC5EA7F") {
    owner {
      nPlaylists
    }
  }
}
```

Optimized:
```
{
  theme(themeId: "116060566904825") {
    coverUrls
    albums(startPoint: 0, itemsToGet: 20) {
      title
      webUri
      squareImage {
        url
      }
    }
  }
}
```

Chart -> New Videos, Classic Videos:
```
{
  chart(chartId: "47217A038CAC4EA69F0C5156F0A8BF49") {
    name
    newVideosSection {
      subgenre {
        title
        id
      }
      generalGenre {
        title
        id
      }
      coverImageUrl
    }
    classicVideosSection {
      subgenre {
        title
        id
      }
      generalGenre {
        title
        id
      }
      coverImageUrl
    }
  }
}
```

Optimized: 1 or N themes:
```
{
  theme(themeId: "196059980955404") {
    id
    title
    genreId
    genre {
      id
      title
      isGeneral
      chartId
    }
  }
}
```

Optimized: N playlists, N albums:
```
{
  userProfile(username: "kaz_piro_piro") {
    playlists(startPoint: 10, itemsToGet: 10) {
      id
      title
      nTracks
      rawGenres
      durationMs
    }
    albums(itemsToGet:10) {
      id
      trackCount {
        trackList
      }
      durationMs
    }     
  }
}
```

Chart first load:
```
{
  chart(chartId: "47217A038CAC4EA69F0C5156F0A8BF49") {
    name
    genre {
      id
      title
    }
    newVideosSection {
      coverImageUrl
      nTracks
      subgenre {
        id
        title
      }
      generalGenre {
        id
        title
      }
    }
    classicVideosSection {
      coverImageUrl
      nTracks
      subgenre {
        id
        title
      }
      generalGenre {
        id
        title
      }
    }
    nTracks
    tracks(startPoint: 0, itemsToGet: 10) {
      id
      title
      coverImage {
        url
      }
      previewUrl
      artistName
      artist {
        id
        name
        webUri
        squareImage {
          url
        }
      }
    }
    nNarratedAlbums
    narratedAlbums(startPoint: 0, itemsToGet: 10) {
      id
      title
      webUri
      squareImage {
        url
      }
      artist {
        id
        name
        webUri
        squareImage {
          url
        }
      }
      topUserNarrative {
        id
        title
        author {
          id
          username
          profilePictureUrl
        }
      }
    }
    nAlbums
    albums(startPoint: 0, itemsToGet: 10) {
      id
      title
      webUri
      squareImage {
        url
      }
      artist {
        id
        name
        webUri
        squareImage {
          url
        }
      }
    }
  }
}
```

Chart second load (playlists will be available later):
```
{
  chart(chartId: "47217A038CAC4EA69F0C5156F0A8BF49") {
    name    
    nArtists
    artists(startPoint: 0, itemsToGet: 10) {
      id
      name
      webUri
      squareImage {
        url
      }
    }
  }
}
```

Themes for genre (here genreId is chart.genre.id in the previous step):
```
{
  genre(genreId: "5984826E7F9C4AC68E12F6C352FFBAAE") {
    title
    nThemes
    themes(startPoint: 0, itemsToGet: 10) {
      title
      coverUrls
    }
  }
}
```

Themes for US 100 (when chart.genre is null):
```
{
  genres(genreType: GENERAL) {
    title
    nThemes
    themes(startPoint: 0, itemsToGet: 10) {
      title
      coverUrls
    }
  }
}
```

General genre -> Classic/New sections:
```
{
  genre(genreId: "5984826E7F9C4AC68E12F6C352FFBAAE") {
    title
    classicVideosSection {
      subgenre {
        id
        title
      }
      coverImageUrl
      nTracks
    }
    newVideosSection {
      subgenre {
        id
        title
      }
      coverImageUrl
      nTracks
    }
  }
}
```

Subgenre -> Classic/New videos:
```
{
  genre(genreId: "E65B5CF51DB84FDCBE087DB71B701009") {
    title
    nNewTracks
    newTracks(startPoint: 0, itemsToGet: 10) {
      id
      title
      artistName
      url
      previewUrl
      artist {
        id
        name
        webUri
      }
      webUri
    }
    nClassicTracks
    classicTracks(startPoint: 0, itemsToGet: 10) {
      id
      title
      artistName
      url
      previewUrl
      artist {
        id
        name
        webUri
      }
      webUri
    }
  }
}
```

Chart page: N playlists:
```
{
  chart(chartId: "97BF03C44B964915A5046EA14666141D") {
    name
    nPlaylists
    playlists(startPoint: 30, itemsToGet: 10) {
      id
      title
      owner {
        id
        username
      }
      coverUrls      
    }
    randomPlaylists(itemsToGet: 5) {
      id
      title
      owner {
        id
        username
      }
      coverUrls
    }
  }
}
```

URI, URL:
```
{
  uriExtractor(url: "https://taylor-swift.vibbidi.net") {
    entityType
    entityUuid
    user {
      username
      id
      webUri
    }
    artist {
      name
      id
      webUri
    }
    album {
      title
      id
      webUri
    }
    chart {
      name
      id
      webUri
    }
    playlist {
      title
      id
      webUri
      coverUrls
    }
    track {
      title
      id
      webUri
    }
  }
}

{
  uriExtractor(url: "https://www.vibbidi.net/artist?id=758EB6EA11C4945098996712EE98E6AB") {
    entityUuid
    entityType
    artist {
      name
    }
  }
}

{
  uriExtractor(url: "https://www.vibbidi.net/single?id=4C41F50DE48144319785975F47599E9F") {
    entityUuid
    entityType
    track {
      title
    }
  }
}

{
  uriExtractor(url: "https://www.vibbidi.net/album?id=BE37449EE0824DAF84FAD69E29BF727B") {
    entityUuid
    entityType
    album {
      title
    }
  }
}

{
  uriExtractor(url: "https://www.vibbidi.net/user?id=498273542225616") {
    entityUuid
    entityType
    user {
      username
    }
  }
}

{
  uriExtractor(url: "https://www.vibbidi.net/user?username=kaz_piro_piro") {
    entityUuid
    entityType
    user {
      profilePictureUrl
    }
  }
}

{
  uriExtractor(url: "https://www.vibbidi.net/playlist?id=0D398E6CA0764CDDA47F770871CAD3DA") {
    entityUuid
    entityType
    playlist {
      id
      title
    }
  }
}

{
  uriExtractor(url: "https://www.vibbidi.net/chart?id=47217A038CAC4EA69F0C5156F0A8BF49") {
    entityUuid
    entityType
    chart {
      name
    }
  }
}
```