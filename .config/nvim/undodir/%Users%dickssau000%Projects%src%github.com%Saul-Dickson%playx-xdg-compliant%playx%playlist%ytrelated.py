Vim�UnDo� ʭ����D�Z��3F1�x��F���Ǿ�Щa   �   7    CACHE_PATH = Path("~/.playx/playlist").expanduser()   �                          _ik    _�                     �       ����                                                                                                                                                                                                                                                                                                                                                             _iT     �   �   �   �      7    CACHE_PATH = Path("~/.playx/playlist").expanduser()5�_�                    �   !    ����                                                                                                                                                                                                                                                                                                                                                             _iW     �   �   �   �      >    CACHE_PATH = Path("~/.cache/.playx/playlist").expanduser()5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             _ia     �   �   �   �      7    CACHE_PATH = Path("~/.playx/playlist").expanduser()5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             _ic     �   �   �   �      6    CACHE_PATH = Path("~/playx/playlist").expanduser()5�_�                     �       ����                                                                                                                                                                                                                                                                                                                                                             _ij    �   4   �   �   R           def __init__(self, url):           super().__init__()           self.url = url   *        # self.url = self._update_URL(URL)           self.playlist_name = ""   @        self.youtube_base = "https://www.youtube.com/watch?v={}"       $    def _get_ytmusic_url(self, url):           """   3        Get the video ID from the URL and add it to   "        the YoutubeMusic base URL.           """   %        video_id = url.split("=")[-1]   F        return "https://music.youtube.com/watch?v={}".format(video_id)       &    def _get_playlist_data(self, url):           """   7        Use YoutubeDL to extract all the songs from the           passed URL.           """           ydl_opts = {               "quiet": True,   '            "nocheckcertificate": True,   %            "dump_single_json": True,   !            "extract_flat": True,   )            "logger": CustomYTDLLogger(),   	        }               # Extract the info now   <        songs = YoutubeDL(ydl_opts).extract_info(url, False)       <        # Extract the songs into the MetaData class' objects   %        for song in songs["entries"]:   H            self.list_content_tuple.append(YoutubeMetadata(song["url"]))   +        self.playlist_name = songs["title"]           def _create_mix(self):           """   ?        In order to get the playlist, we need to make a request           to youtube music.   B        YT Music uses JS to automatically update the page URL with           the playlist ID.   ,        This is when we extract the list ID.       B        Since it does all of it using JS, we can't use requests or           someting similar.           """   +        logger.info("Using YTMusic Method")   #        driver = self._get_driver()           driver.get(self.url)   V        WebDriverWait(driver, 10).until(lambda driver: driver.current_url != self.url)       '        # The URL should now be updated   (        updated_url = driver.current_url   0        playlist_id = updated_url.split("=")[-1]   U        playlist_url = "https://www.youtube.com/playlist?list={}".format(playlist_id)   -        self._get_playlist_data(playlist_url)           def _not_name(self, name):           """   D        Check the passed name to see if its actually a name of song.       C        While extracting sometimes playlists are suggested in which   E        the extraction algo extracts the time of the playlist instead   D        of the name, so we need to remove it from the list of songs.           """   9        match = re.match(r"[0-9][0-9]?:[0-9][0-9]", name)           if match is None:               return False           else:               return True           def _get_driver(self):   "        chrome_options = Options()   1        chrome_options.add_argument("--headless")   3        chrome_options.add_argument("--no-sandbox")   ?        chrome_options.add_argument("–disable-dev-shm-usage")   ;        chrome_options.add_argument("--disable-extensions")   B        chrome_options.add_argument("--ignore-certificate-errors")   C        chrome_options.add_argument("--remote-debugging-port=9222")   X        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])5��