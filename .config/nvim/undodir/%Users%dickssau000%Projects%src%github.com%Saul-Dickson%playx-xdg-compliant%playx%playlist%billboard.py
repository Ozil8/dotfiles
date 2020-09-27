Vim�UnDo� �!�o�+�oȆ�O���g7��QT��9������   �   5    print(get_chart_names("~/.playx/logs/billboard"))   �                          _io    _�                     �       ����                                                                                                                                                                                                                                                                                                                                                             _ic     �   �              5    print(get_chart_names("~/.playx/logs/billboard"))5�_�                    �   *    ����                                                                                                                                                                                                                                                                                                                                                             _ig     �   �              B    print(get_chart_names("~/.local/share/.playx/logs/billboard"))5�_�                    �   0    ����                                                                                                                                                                                                                                                                                                                                                             _ij     �   �              A    print(get_chart_names("~/.local/share/playx/logs/billboard"))5�_�                    �   0    ����                                                                                                                                                                                                                                                                                                                                                             _ij     �   �              @    print(get_chart_names("~/.local/share/playx/ogs/billboard"))5�_�                    �   0    ����                                                                                                                                                                                                                                                                                                                                                             _ij     �   �              ?    print(get_chart_names("~/.local/share/playx/gs/billboard"))5�_�                    �   0    ����                                                                                                                                                                                                                                                                                                                                                             _ij     �   �              >    print(get_chart_names("~/.local/share/playx/s/billboard"))5�_�                    �   0    ����                                                                                                                                                                                                                                                                                                                                                             _ik     �   �              =    print(get_chart_names("~/.local/share/playx//billboard"))5�_�                     �   !    ����                                                                                                                                                                                                                                                                                                                                                             _in    �      ]   �   b       import requests   from bs4 import BeautifulSoup   	import re   	import os       Ffrom playx.playlist.playlistbase import PlaylistBase, SongMetadataBase       from playx.logger import Logger       # Setup logger   logger = Logger("Billboard")           """   __author__ = Deepjyoti Barman   #__github__ = github.com/deepjyoti30       """           class Song(SongMetadataBase):   &    """Class to store song details."""       4    def __init__(self, title="", artist="", rank=0):           super().__init__()           self.title = title           self.artist = artist           self.rank = rank   $        self._create_search_querry()   !        self._remove_duplicates()       $    def _create_search_querry(self):           """   C        Create a search querry using the title and the artist name.           """   :        self.search_query = self.title + " " + self.artist           class BillboardIE:   *    """Class to store billboard charts."""           def __init__(self, URL):   '        """Initiate the basic stuff."""   :        self.baseurl = "https://www.billboard.com/charts/"   %        self.URL = self.baseurl + URL   #        self.soup = self.get_soup()           self.chart = []           self.chart_name = ""            self.get_name_of_chart()           self.get_chart()           self.replace_symbols()           def get_soup(self):   /        """Return the soup for the response."""   )        response = requests.get(self.URL)   :        soup = BeautifulSoup(response.text, "html.parser")           return soup           def replace_symbols(self):   .        """Replace symbols like &amp with &"""           for i in self.chart:   3            i.title = re.sub(r"&amp", "&", i.title)   5            i.artist = re.sub(r"&amp", "&", i.artist)            def get_name_of_chart(self):   9        """Get the name of the chart from the webpage."""   R        name = self.soup.findAll("h1", attrs={"class": "charts-hero__chart-name"})   5        name = name[0].findAll('span')[0].contents[0]           logger.debug(name)           self.chart_name = name           def get_chart(self):   9        """New method to extract billboard chart data."""   +        chart_contents = self.soup.findAll(   !                            "li",   B                            attrs={"class": "chart-list__element"}                           )       ,        for chart_element in chart_contents:   )            rank = chart_element.findAll(   #                            'span',   J                            attrs={'class': 'chart-element__rank__number'}   (                        )[0].contents[0]   *            track = chart_element.findAll(   #                            'span',   O                            attrs={'class': 'chart-element__information__song'}   (                        )[0].contents[0]   +            artist = chart_element.findAll(   #                            'span',   Q                            attrs={'class': 'chart-element__information__artist'}   (                        )[0].contents[0]   8            self.chart.append(Song(track, artist, rank))           &class BillboardPlaylist(PlaylistBase):   0    """Class to store Billboards Charts data."""    5��