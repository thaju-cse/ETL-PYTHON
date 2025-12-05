Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
help(git)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    help(git)
NameError: name 'git' is not defined

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
hello world

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
hello world

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
testing

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Started Extraction of data..
Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 45, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 38, in main
    table_data_frame = extracting(url, head)
  File "E:/Data Engineer/projects/world_bank_practice.py", line 25, in extracting
    table_data_frame.loc[len(table_data_frame)] = row_list
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 911, in __setitem__
    iloc._setitem_with_indexer(indexer, value, self.name)
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 1932, in _setitem_with_indexer
    self._setitem_with_indexer_missing(indexer, value)
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 2306, in _setitem_with_indexer_missing
    raise ValueError("cannot set a row with mismatched columns")
ValueError: cannot set a row with mismatched columns

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Started Extraction of data..
['1']
['1', ' China']
['1', ' China', '21\n']
['2']
['2', ' United States']
['2', ' United States', '13\n']
['3']
['3', ' Japan']
['3', ' Japan', '8\n']
['4\n']
['4\n', ' Canada']
['4\n', ' Canada', '6\n']
[' France']
[' France', '6\n']
Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 45, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 38, in main
    table_data_frame = extracting(url, head)
  File "E:/Data Engineer/projects/world_bank_practice.py", line 25, in extracting
    table_data_frame.loc[len(table_data_frame)] = row_list
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 911, in __setitem__
    iloc._setitem_with_indexer(indexer, value, self.name)
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 1932, in _setitem_with_indexer
    self._setitem_with_indexer_missing(indexer, value)
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 2306, in _setitem_with_indexer_missing
    raise ValueError("cannot set a row with mismatched columns")
ValueError: cannot set a row with mismatched columns

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Started Extraction of data..
[<tr>
<th>Rank</th>
<th>Country</th>
<th>Number
</th></tr>, <tr>
<td>1</td>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/40px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/60px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/China" title="China">China</a></td>
<td>21
</td></tr>, <tr>
<td>2</td>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/40px-Flag_of_the_United_States.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/60px-Flag_of_the_United_States.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/United_States" title="United States">United States</a></td>
<td>13
</td></tr>, <tr>
<td>3</td>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/40px-Flag_of_Japan.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/60px-Flag_of_Japan.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Japan" title="Japan">Japan</a></td>
<td>8
</td></tr>, <tr>
<td rowspan="3">4
</td>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Canada_%28Pantone%29.svg/40px-Flag_of_Canada_%28Pantone%29.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Canada_%28Pantone%29.svg/60px-Flag_of_Canada_%28Pantone%29.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Canada" title="Canada">Canada</a></td>
<td>6
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/40px-Flag_of_France.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/60px-Flag_of_France.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/France" title="France">France</a></td>
<td>6
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/40px-Flag_of_the_United_Kingdom.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/60px-Flag_of_the_United_Kingdom.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/United_Kingdom" title="United Kingdom">United Kingdom</a></td>
<td>6
</td></tr>, <tr>
<td>7</td>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/40px-Flag_of_South_Korea.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/60px-Flag_of_South_Korea.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/South_Korea" title="South Korea">South Korea</a></td>
<td>5
</td></tr>, <tr>
<td rowspan="2">8
</td>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="640" data-file-width="1280" decoding="async" height="12" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Flag_of_Australia_%28converted%29.svg/40px-Flag_of_Australia_%28converted%29.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Flag_of_Australia_%28converted%29.svg/60px-Flag_of_Australia_%28converted%29.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Australia" title="Australia">Australia</a></td>
<td>4
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/60px-Flag_of_Germany.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Germany" title="Germany">Germany</a></td>
<td>4
</td></tr>, <tr>
<td rowspan="4">10
</td>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="700" data-file-width="1000" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/40px-Flag_of_Brazil.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/60px-Flag_of_Brazil.svg.png 2x" width="22"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Brazil" title="Brazil">Brazil</a></td>
<td>3
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/60px-Flag_of_the_Netherlands.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Netherlands" title="Netherlands">Netherlands</a></td>
<td>3
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/40px-Flag_of_Singapore.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/60px-Flag_of_Singapore.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Singapore" title="Singapore">Singapore</a></td>
<td>3
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="500" data-file-width="750" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/60px-Flag_of_Spain.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Spain" title="Spain">Spain</a></td>
<td>3
</td></tr>, <tr>
<td rowspan="4">14
</td>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/40px-Flag_of_India.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/60px-Flag_of_India.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/India" title="India">India</a></td>
<td>2
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="1000" data-file-width="1500" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/0/03/Flag_of_Italy.svg/60px-Flag_of_Italy.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Italy" title="Italy">Italy</a></td>
<td>2
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/40px-Flag_of_Russia.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/60px-Flag_of_Russia.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Russia" title="Russia">Russia</a></td>
<td>2
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="16" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/20px-Flag_of_Switzerland_%28Pantone%29.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/40px-Flag_of_Switzerland_%28Pantone%29.svg.png 1.5x" width="16"/></span></span>  </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Switzerland" title="Switzerland">Switzerland</a></td>
<td>2
</td></tr>, <tr>
<td rowspan="7">18
</td>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/40px-Flag_of_Austria.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/60px-Flag_of_Austria.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Austria" title="Austria">Austria</a></td>
<td>1
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/40px-Flag_of_Belgium_%28civil%29.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/60px-Flag_of_Belgium_%28civil%29.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Belgium" title="Belgium">Belgium</a></td>
<td>1
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="387" data-file-width="512" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/20px-Flag_of_Denmark.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/40px-Flag_of_Denmark.svg.png 1.5x" width="20"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Denmark" title="Denmark">Denmark</a></td>
<td>1
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="1100" data-file-width="1800" decoding="async" height="14" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Finland.svg/40px-Flag_of_Finland.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Finland.svg/60px-Flag_of_Finland.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Finland" title="Finland">Finland</a></td>
<td>1
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="550" data-file-width="1400" decoding="async" height="9" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Flag_of_Qatar.svg/40px-Flag_of_Qatar.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Flag_of_Qatar.svg/60px-Flag_of_Qatar.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Qatar" title="Qatar">Qatar</a></td>
<td>1
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="1000" data-file-width="1600" decoding="async" height="14" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Flag_of_Sweden.svg/40px-Flag_of_Sweden.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Flag_of_Sweden.svg/60px-Flag_of_Sweden.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/Sweden" title="Sweden">Sweden</a></td>
<td>1
</td></tr>, <tr>
<td><span class="flagicon nowrap"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_United_Arab_Emirates.svg/40px-Flag_of_the_United_Arab_Emirates.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_United_Arab_Emirates.svg/60px-Flag_of_the_United_Arab_Emirates.svg.png 2x" width="23"/></span></span> </span><a href="/web/20251007065341/https://en.wikipedia.org/wiki/United_Arab_Emirates" title="United Arab Emirates">United Arab Emirates</a></td>
<td>1
</td></tr>]
['1']
['1', ' China']
['1', ' China', '21\n']
['2']
['2', ' United States']
['2', ' United States', '13\n']
['3']
['3', ' Japan']
['3', ' Japan', '8\n']
['4\n']
['4\n', ' Canada']
['4\n', ' Canada', '6\n']
[' France']
[' France', '6\n']
Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 46, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 39, in main
    table_data_frame = extracting(url, head)
  File "E:/Data Engineer/projects/world_bank_practice.py", line 26, in extracting
    table_data_frame.loc[len(table_data_frame)] = row_list
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 911, in __setitem__
    iloc._setitem_with_indexer(indexer, value, self.name)
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 1932, in _setitem_with_indexer
    self._setitem_with_indexer_missing(indexer, value)
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 2306, in _setitem_with_indexer_missing
    raise ValueError("cannot set a row with mismatched columns")
ValueError: cannot set a row with mismatched columns

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Started Extraction of data..

['1\n']
['1\n', ' Industrial and Commercial Bank of China\n']
['1\n', ' Industrial and Commercial Bank of China\n', '6,688.74\n']
['2\n']
['2\n', ' Agricultural Bank of China\n']
['2\n', ' Agricultural Bank of China\n', '5,923.76\n']
['3\n']
['3\n', ' China Construction Bank\n']
['3\n', ' China Construction Bank\n', '5,558.38\n']
['4\n']
['4\n', ' Bank of China\n']
['4\n', ' Bank of China\n', '4,803.51\n']
['5\n']
['5\n', ' JPMorgan Chase\n']
['5\n', ' JPMorgan Chase\n', '4,002.81\n']
['6\n']
['6\n', ' Bank of America\n']
['6\n', ' Bank of America\n', '3,261.52\n']
['7\n']
['7\n', ' HSBC\n']
['7\n', ' HSBC\n', '2,989.81\n']
['8\n']
['8\n', ' BNP Paribas\n']
['8\n', ' BNP Paribas\n', '2,809.83\n']
['9\n']
['9\n', ' Crédit Agricole\n']
['9\n', ' Crédit Agricole\n', '2,693.58\n']
['10\n']
['10\n', ' Mitsubishi UFJ Financial Group\n']
['10\n', ' Mitsubishi UFJ Financial Group\n', '2,628.12\n']
['11\n']
['11\n', ' Postal Savings Bank of China\n']
['11\n', ' Postal Savings Bank of China\n', '2,340.69\n']
['12\n']
['12\n', ' Citigroup\n']
['12\n', ' Citigroup\n', '2,151.95\n']
['13\n']
['13\n', ' Bank of Communications\n']
['13\n', ' Bank of Communications\n', '2,041.45\n']
['14\n']
['14\n', ' SMBC Group\n']
['14\n', ' SMBC Group\n', '1,977.18\n']
['15\n']
['15\n', ' Wells Fargo\n']
['15\n', ' Wells Fargo\n', '1,929.85\n']
['16\n']
['16\n', ' Banco Santander\n']
['16\n', ' Banco Santander\n', '1,901.94\n']
['17\n']
['17\n', ' Barclays\n']
['17\n', ' Barclays\n', '1,900.67\n']
['18\n']
['18\n', ' Mizuho Financial Group\n']
['18\n', ' Mizuho Financial Group\n', '1,805.52\n']
['19\n']
['19\n', ' Goldman Sachs\n']
['19\n', ' Goldman Sachs\n', '1,675.97\n']
['20\n']
['20\n', ' China Merchants Bank\n']
['20\n', ' China Merchants Bank\n', '1,664.87\n']
['21\n']
['21\n', ' Groupe BPCE\n']
['21\n', ' Groupe BPCE\n', '1,646.53\n']
['22\n']
['22\n', ' Société Générale\n']
['22\n', ' Société Générale\n', '1,601.74\n']
['23\n']
['23\n', ' UBS\n']
['23\n', ' UBS\n', '1,563.32\n']
['24\n']
['24\n', ' Japan Post Bank\n']
['24\n', ' Japan Post Bank\n', '1,546.95\n']
['25\n']
['25\n', ' Royal Bank of Canada\n']
['25\n', ' Royal Bank of Canada\n', '1,513.86\n']
['26\n']
['26\n', ' Toronto-Dominion Bank\n']
['26\n', ' Toronto-Dominion Bank\n', '1,446.51\n']
['27\n']
['27\n', ' Industrial Bank\n']
['27\n', ' Industrial Bank\n', '1,439.62\n']
['28\n']
['28\n', ' Deutsche Bank\n']
['28\n', ' Deutsche Bank\n', '1,436.15\n']
['29\n']
['29\n', ' China CITIC Bank\n']
['29\n', ' China CITIC Bank\n', '1,306.01\n']
['30\n']
['30\n', ' Shanghai Pudong Development Bank\n']
['30\n', ' Shanghai Pudong Development Bank\n', '1,296.31\n']
['31\n']
['31\n', ' Crédit Mutuel\n']
['31\n', ' Crédit Mutuel\n', '1,252.10\n']
['32\n']
['32\n', ' Morgan Stanley\n']
['32\n', ' Morgan Stanley\n', '1,215.07\n']
['33\n']
['33\n', ' Lloyds Banking Group\n']
['33\n', ' Lloyds Banking Group\n', '1,135.12\n']
['34\n']
['34\n', ' China Minsheng Bank\n']
['34\n', ' China Minsheng Bank\n', '1,070.68\n']
['35\n']
['35\n', ' ING Group\n']
['35\n', ' ING Group\n', '1,056.57\n']
['36\n']
['36\n', ' Bank of Montreal\n']
['36\n', ' Bank of Montreal\n', '1,014.36\n']
['37\n']
['37\n', ' Scotiabank\n']
['37\n', ' Scotiabank\n', '978.47\n']
['38\n']
['38\n', ' Intesa Sanpaolo\n']
['38\n', ' Intesa Sanpaolo\n', '966.23\n']
['39\n']
['39\n', ' China Everbright Bank\n']
['39\n', ' China Everbright Bank\n', '953.41\n']
['40\n']
['40\n', ' NatWest Group\n']
['40\n', ' NatWest Group\n', '886.34\n']
['41\n']
['41\n', ' ANZ Group\n']
['41\n', ' ANZ Group\n', '852.19\n']
['42\n']
['42\n', ' Standard Chartered\n']
['42\n', ' Standard Chartered\n', '849.69\n']
['43\n']
['43\n', ' State Bank of India\n']
['43\n', ' State Bank of India\n', '846.64\n']
['44\n']
['44\n', ' UniCredit\n']
['44\n', ' UniCredit\n', '811.68\n']
['45\n']
['45\n', ' Commonwealth Bank\n']
['45\n', ' Commonwealth Bank\n', '809.81\n']
['46\n']
['46\n', ' Banco Bilbao Vizcaya Argentaria\n']
['46\n', ' Banco Bilbao Vizcaya Argentaria\n', '799.67\n']
['47\n']
['47\n', ' Ping An Bank\n']
['47\n', ' Ping An Bank\n', '790.41\n']
['48\n']
['48\n', ' La Banque postale\n']
['48\n', ' La Banque postale\n', '766.91\n']
['49\n']
['49\n', ' National Australia Bank\n']
['49\n', ' National Australia Bank\n', '748.98\n']
['50\n']
['50\n', ' Canadian Imperial Bank of Commerce\n']
['50\n', ' Canadian Imperial Bank of Commerce\n', '747.91\n']
['51\n']
['51\n', ' Westpac\n']
['51\n', ' Westpac\n', '747.10\n']
['52\n']
['52\n', ' DZ Bank\n']
['52\n', ' DZ Bank\n', '682.93\n']
['53\n']
['53\n', ' U.S. Bancorp\n']
['53\n', ' U.S. Bancorp\n', '678.32\n']
['54\n']
['54\n', ' CaixaBank\n']
['54\n', ' CaixaBank\n', '653.28\n']
['55\n']
['55\n', ' Rabobank\n']
['55\n', ' Rabobank\n', '651.47\n']
['56\n']
['56\n', ' Nordea\n']
['56\n', ' Nordea\n', '645.36\n']
['57\n']
['57\n', ' Capital One\n']
['57\n', ' Capital One\n', '637.78\n']
['58\n']
['58\n', ' DBS Group\n']
['58\n', ' DBS Group\n', '606.13\n']
['59\n']
['59\n', ' Huaxia Bank\n']
['59\n', ' Huaxia Bank\n', '599.59\n']
['60\n']
['60\n', ' Commerzbank\n']
['60\n', ' Commerzbank\n', '574.23\n']
['61\n']
['61\n', ' Bank of Beijing\n']
['61\n', ' Bank of Beijing\n', '574.14\n']
['62\n']
['62\n', ' Norinchukin Bank\n']
['62\n', ' Norinchukin Bank\n', '560.75\n']
['63\n']
['63\n', ' PNC Financial Services\n']
['63\n', ' PNC Financial Services\n', '560.04\n']
['64\n']
['64\n', ' Sberbank of Russia\n']
['64\n', ' Sberbank of Russia\n', '557.48\n']
['65\n']
['65\n', ' Bank of Jiangsu\n']
['65\n', ' Bank of Jiangsu\n', '541.41\n']
['66\n']
['66\n', ' Truist Financial Corp\n']
['66\n', ' Truist Financial Corp\n', '531.18\n']
['67\n']
['67\n', ' Danske Bank\n']
['67\n', ' Danske Bank\n', '515.87\n']
['68\n']
['68\n', ' KB Financial Group\n']
['68\n', ' KB Financial Group\n', '513.01\n']
['69\n']
['69\n', ' Shinhan Financial Group\n']
['69\n', ' Shinhan Financial Group\n', '500.77\n']
['70\n']
['70\n', ' Nationwide Building Society\n']
['70\n', ' Nationwide Building Society\n', '498.77\n']
['71\n']
['71\n', ' Sumitomo Mitsui Trust Holdings\n']
['71\n', ' Sumitomo Mitsui Trust Holdings\n', '498.16\n']
['72\n']
['72\n', ' China Guangfa Bank\n']
['72\n', ' China Guangfa Bank\n', '494.93\n']
['73\n']
['73\n', ' HDFC Bank\n']
['73\n', ' HDFC Bank\n', '494.06\n']
['74\n']
['74\n', ' Itaú Unibanco\n']
['74\n', ' Itaú Unibanco\n', '492.90\n']
['75\n']
['75\n', ' Resona Holdings\n']
['75\n', ' Resona Holdings\n', '491.13\n']
['76\n']
['76\n', ' Charles Schwab Corporation\n']
['76\n', ' Charles Schwab Corporation\n', '479.84\n']
['77\n']
['77\n', ' Oversea-Chinese Banking Corporation\n']
['77\n', ' Oversea-Chinese Banking Corporation\n', '458.00\n']
['78\n']
['78\n', ' China Zheshang Bank\n']
['78\n', ' China Zheshang Bank\n', '455.61\n']
['79\n']
['79\n', ' Bank of Shanghai\n']
['79\n', ' Bank of Shanghai\n', '442.06\n']
['80\n']
['80\n', ' Hana Financial Group\n']
['80\n', ' Hana Financial Group\n', '431.78\n']
['81\n']
['81\n', ' Bank of Ningbo\n']
['81\n', ' Bank of Ningbo\n', '428.16\n']
['82\n']
['82\n', ' Nonghyup Bank\n']
['82\n', ' Nonghyup Bank\n', '419.37\n']
['83\n']
['83\n', ' BNY Mellon\n']
['83\n', ' BNY Mellon\n', '416.06\n']
['84\n']
['84\n', ' ABN AMRO\n']
['84\n', ' ABN AMRO\n', '411.66\n']
['85\n']
['85\n', ' United Overseas Bank\n']
['85\n', ' United Overseas Bank\n', '393.97\n']
['86\n']
['86\n', ' Banco do Brasil\n']
['86\n', ' Banco do Brasil\n', '393.52\n']
['87\n']
['87\n', ' Woori Financial Group\n']
['87\n', ' Woori Financial Group\n', '393.34\n']
['88\n']
['88\n', ' KBC Group\n']
['88\n', ' KBC Group\n', '386.22\n']
['89\n']
['89\n', ' Nomura Holdings\n']
['89\n', ' Nomura Holdings\n', '385.00\n']
['90\n']
['90\n', ' Landesbank Baden-Württemberg\n']
['90\n', ' Landesbank Baden-Württemberg\n', '368.98\n']
['91\n']
['91\n', ' Erste Group\n']
['91\n', ' Erste Group\n', '366.22\n']
['92\n']
['92\n', ' National Bank of Canada\n']
['92\n', ' National Bank of Canada\n', '365.25\n']
['93\n']
['93\n', ' State Street Corporation\n']
['93\n', ' State Street Corporation\n', '362.95\n']
['94\n']
['94\n', ' Qatar National Bank\n']
['94\n', ' Qatar National Bank\n', '356.52\n']
['95\n']
['95\n', ' Bank of Nanjing\n']
['95\n', ' Bank of Nanjing\n', '355.03\n']
['96\n']
['96\n', ' SEB Group\n']
['96\n', ' SEB Group\n', '339.65\n']
['97\n']
['97\n', ' Raiffeisen Group\n']
['97\n', ' Raiffeisen Group\n', '337.25\n']
['98\n']
['98\n', ' Banco Bradesco\n']
['98\n', ' Banco Bradesco\n', '331.96\n']
['99\n']
['99\n', ' VTB Bank\n']
['99\n', ' VTB Bank\n', '330.43\n']
['100\n']
['100\n', ' First Abu Dhabi Bank\n']
['100\n', ' First Abu Dhabi Bank\n', '330.32\n']
Data frame creation Successful..

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
['2\n']
['2\n', ' Agricultural Bank of China\n']
['2\n', ' Agricultural Bank of China\n', '5,923.76\n']
['3\n']
['3\n', ' China Construction Bank\n']
['3\n', ' China Construction Bank\n', '5,558.38\n']
['4\n']
['4\n', ' Bank of China\n']
['4\n', ' Bank of China\n', '4,803.51\n']
['5\n']
['5\n', ' JPMorgan Chase\n']
['5\n', ' JPMorgan Chase\n', '4,002.81\n']
['6\n']
['6\n', ' Bank of America\n']
['6\n', ' Bank of America\n', '3,261.52\n']
['7\n']
['7\n', ' HSBC\n']
['7\n', ' HSBC\n', '2,989.81\n']
['8\n']
['8\n', ' BNP Paribas\n']
['8\n', ' BNP Paribas\n', '2,809.83\n']
['9\n']
['9\n', ' Crédit Agricole\n']
['9\n', ' Crédit Agricole\n', '2,693.58\n']
['10\n']
['10\n', ' Mitsubishi UFJ Financial Group\n']
['10\n', ' Mitsubishi UFJ Financial Group\n', '2,628.12\n']
['11\n']
['11\n', ' Postal Savings Bank of China\n']
['11\n', ' Postal Savings Bank of China\n', '2,340.69\n']
['12\n']
['12\n', ' Citigroup\n']
['12\n', ' Citigroup\n', '2,151.95\n']
['13\n']
['13\n', ' Bank of Communications\n']
['13\n', ' Bank of Communications\n', '2,041.45\n']
['14\n']
['14\n', ' SMBC Group\n']
['14\n', ' SMBC Group\n', '1,977.18\n']
['15\n']
['15\n', ' Wells Fargo\n']
['15\n', ' Wells Fargo\n', '1,929.85\n']
['16\n']
['16\n', ' Banco Santander\n']
['16\n', ' Banco Santander\n', '1,901.94\n']
['17\n']
['17\n', ' Barclays\n']
['17\n', ' Barclays\n', '1,900.67\n']
['18\n']
['18\n', ' Mizuho Financial Group\n']
['18\n', ' Mizuho Financial Group\n', '1,805.52\n']
['19\n']
['19\n', ' Goldman Sachs\n']
['19\n', ' Goldman Sachs\n', '1,675.97\n']
['20\n']
['20\n', ' China Merchants Bank\n']
['20\n', ' China Merchants Bank\n', '1,664.87\n']
['21\n']
['21\n', ' Groupe BPCE\n']
['21\n', ' Groupe BPCE\n', '1,646.53\n']
['22\n']
['22\n', ' Société Générale\n']
['22\n', ' Société Générale\n', '1,601.74\n']
['23\n']
['23\n', ' UBS\n']
['23\n', ' UBS\n', '1,563.32\n']
['24\n']
['24\n', ' Japan Post Bank\n']
['24\n', ' Japan Post Bank\n', '1,546.95\n']
['25\n']
['25\n', ' Royal Bank of Canada\n']
['25\n', ' Royal Bank of Canada\n', '1,513.86\n']
['26\n']
['26\n', ' Toronto-Dominion Bank\n']
['26\n', ' Toronto-Dominion Bank\n', '1,446.51\n']
['27\n']
['27\n', ' Industrial Bank\n']
['27\n', ' Industrial Bank\n', '1,439.62\n']
['28\n']
['28\n', ' Deutsche Bank\n']
['28\n', ' Deutsche Bank\n', '1,436.15\n']
['29\n']
['29\n', ' China CITIC Bank\n']
['29\n', ' China CITIC Bank\n', '1,306.01\n']
['30\n']
['30\n', ' Shanghai Pudong Development Bank\n']
['30\n', ' Shanghai Pudong Development Bank\n', '1,296.31\n']
['31\n']
['31\n', ' Crédit Mutuel\n']
['31\n', ' Crédit Mutuel\n', '1,252.10\n']
['32\n']
['32\n', ' Morgan Stanley\n']
['32\n', ' Morgan Stanley\n', '1,215.07\n']
['33\n']
['33\n', ' Lloyds Banking Group\n']
['33\n', ' Lloyds Banking Group\n', '1,135.12\n']
['34\n']
['34\n', ' China Minsheng Bank\n']
['34\n', ' China Minsheng Bank\n', '1,070.68\n']
['35\n']
['35\n', ' ING Group\n']
['35\n', ' ING Group\n', '1,056.57\n']
['36\n']
['36\n', ' Bank of Montreal\n']
['36\n', ' Bank of Montreal\n', '1,014.36\n']
['37\n']
['37\n', ' Scotiabank\n']
['37\n', ' Scotiabank\n', '978.47\n']
['38\n']
['38\n', ' Intesa Sanpaolo\n']
['38\n', ' Intesa Sanpaolo\n', '966.23\n']
['39\n']
['39\n', ' China Everbright Bank\n']
['39\n', ' China Everbright Bank\n', '953.41\n']
['40\n']
['40\n', ' NatWest Group\n']
['40\n', ' NatWest Group\n', '886.34\n']
['41\n']
['41\n', ' ANZ Group\n']
['41\n', ' ANZ Group\n', '852.19\n']
['42\n']
['42\n', ' Standard Chartered\n']
['42\n', ' Standard Chartered\n', '849.69\n']
['43\n']
['43\n', ' State Bank of India\n']
['43\n', ' State Bank of India\n', '846.64\n']
['44\n']
['44\n', ' UniCredit\n']
['44\n', ' UniCredit\n', '811.68\n']
['45\n']
['45\n', ' Commonwealth Bank\n']
['45\n', ' Commonwealth Bank\n', '809.81\n']
['46\n']
['46\n', ' Banco Bilbao Vizcaya Argentaria\n']
['46\n', ' Banco Bilbao Vizcaya Argentaria\n', '799.67\n']
['47\n']
['47\n', ' Ping An Bank\n']
['47\n', ' Ping An Bank\n', '790.41\n']
['48\n']
['48\n', ' La Banque postale\n']
['48\n', ' La Banque postale\n', '766.91\n']
['49\n']
['49\n', ' National Australia Bank\n']
['49\n', ' National Australia Bank\n', '748.98\n']
['50\n']
['50\n', ' Canadian Imperial Bank of Commerce\n']
['50\n', ' Canadian Imperial Bank of Commerce\n', '747.91\n']
['51\n']
['51\n', ' Westpac\n']
['51\n', ' Westpac\n', '747.10\n']
['52\n']
['52\n', ' DZ Bank\n']
['52\n', ' DZ Bank\n', '682.93\n']
['53\n']
['53\n', ' U.S. Bancorp\n']
['53\n', ' U.S. Bancorp\n', '678.32\n']
['54\n']
['54\n', ' CaixaBank\n']
['54\n', ' CaixaBank\n', '653.28\n']
['55\n']
['55\n', ' Rabobank\n']
['55\n', ' Rabobank\n', '651.47\n']
['56\n']
['56\n', ' Nordea\n']
['56\n', ' Nordea\n', '645.36\n']
['57\n']
['57\n', ' Capital One\n']
['57\n', ' Capital One\n', '637.78\n']
['58\n']
['58\n', ' DBS Group\n']
['58\n', ' DBS Group\n', '606.13\n']
['59\n']
['59\n', ' Huaxia Bank\n']
['59\n', ' Huaxia Bank\n', '599.59\n']
['60\n']
['60\n', ' Commerzbank\n']
['60\n', ' Commerzbank\n', '574.23\n']
['61\n']
['61\n', ' Bank of Beijing\n']
['61\n', ' Bank of Beijing\n', '574.14\n']
['62\n']
['62\n', ' Norinchukin Bank\n']
['62\n', ' Norinchukin Bank\n', '560.75\n']
['63\n']
['63\n', ' PNC Financial Services\n']
['63\n', ' PNC Financial Services\n', '560.04\n']
['64\n']
['64\n', ' Sberbank of Russia\n']
['64\n', ' Sberbank of Russia\n', '557.48\n']
['65\n']
['65\n', ' Bank of Jiangsu\n']
['65\n', ' Bank of Jiangsu\n', '541.41\n']
['66\n']
['66\n', ' Truist Financial Corp\n']
['66\n', ' Truist Financial Corp\n', '531.18\n']
['67\n']
['67\n', ' Danske Bank\n']
['67\n', ' Danske Bank\n', '515.87\n']
['68\n']
['68\n', ' KB Financial Group\n']
['68\n', ' KB Financial Group\n', '513.01\n']
['69\n']
['69\n', ' Shinhan Financial Group\n']
['69\n', ' Shinhan Financial Group\n', '500.77\n']
['70\n']
['70\n', ' Nationwide Building Society\n']
['70\n', ' Nationwide Building Society\n', '498.77\n']
['71\n']
['71\n', ' Sumitomo Mitsui Trust Holdings\n']
['71\n', ' Sumitomo Mitsui Trust Holdings\n', '498.16\n']
['72\n']
['72\n', ' China Guangfa Bank\n']
['72\n', ' China Guangfa Bank\n', '494.93\n']
['73\n']
['73\n', ' HDFC Bank\n']
['73\n', ' HDFC Bank\n', '494.06\n']
['74\n']
['74\n', ' Itaú Unibanco\n']
['74\n', ' Itaú Unibanco\n', '492.90\n']
['75\n']
['75\n', ' Resona Holdings\n']
['75\n', ' Resona Holdings\n', '491.13\n']
['76\n']
['76\n', ' Charles Schwab Corporation\n']
['76\n', ' Charles Schwab Corporation\n', '479.84\n']
['77\n']
['77\n', ' Oversea-Chinese Banking Corporation\n']
['77\n', ' Oversea-Chinese Banking Corporation\n', '458.00\n']
['78\n']
['78\n', ' China Zheshang Bank\n']
['78\n', ' China Zheshang Bank\n', '455.61\n']
['79\n']
['79\n', ' Bank of Shanghai\n']
['79\n', ' Bank of Shanghai\n', '442.06\n']
['80\n']
['80\n', ' Hana Financial Group\n']
['80\n', ' Hana Financial Group\n', '431.78\n']
['81\n']
['81\n', ' Bank of Ningbo\n']
['81\n', ' Bank of Ningbo\n', '428.16\n']
['82\n']
['82\n', ' Nonghyup Bank\n']
['82\n', ' Nonghyup Bank\n', '419.37\n']
['83\n']
['83\n', ' BNY Mellon\n']
['83\n', ' BNY Mellon\n', '416.06\n']
['84\n']
['84\n', ' ABN AMRO\n']
['84\n', ' ABN AMRO\n', '411.66\n']
['85\n']
['85\n', ' United Overseas Bank\n']
['85\n', ' United Overseas Bank\n', '393.97\n']
['86\n']
['86\n', ' Banco do Brasil\n']
['86\n', ' Banco do Brasil\n', '393.52\n']
['87\n']
['87\n', ' Woori Financial Group\n']
['87\n', ' Woori Financial Group\n', '393.34\n']
['88\n']
['88\n', ' KBC Group\n']
['88\n', ' KBC Group\n', '386.22\n']
['89\n']
['89\n', ' Nomura Holdings\n']
['89\n', ' Nomura Holdings\n', '385.00\n']
['90\n']
['90\n', ' Landesbank Baden-Württemberg\n']
['90\n', ' Landesbank Baden-Württemberg\n', '368.98\n']
['91\n']
['91\n', ' Erste Group\n']
['91\n', ' Erste Group\n', '366.22\n']
['92\n']
['92\n', ' National Bank of Canada\n']
['92\n', ' National Bank of Canada\n', '365.25\n']
['93\n']
['93\n', ' State Street Corporation\n']
['93\n', ' State Street Corporation\n', '362.95\n']
['94\n']
['94\n', ' Qatar National Bank\n']
['94\n', ' Qatar National Bank\n', '356.52\n']
['95\n']
['95\n', ' Bank of Nanjing\n']
['95\n', ' Bank of Nanjing\n', '355.03\n']
['96\n']
['96\n', ' SEB Group\n']
['96\n', ' SEB Group\n', '339.65\n']
['97\n']
['97\n', ' Raiffeisen Group\n']
['97\n', ' Raiffeisen Group\n', '337.25\n']
['98\n']
['98\n', ' Banco Bradesco\n']
['98\n', ' Banco Bradesco\n', '331.96\n']
['99\n']
['99\n', ' VTB Bank\n']
['99\n', ' VTB Bank\n', '330.43\n']
['100\n']
['100\n', ' First Abu Dhabi Bank\n']
['100\n', ' First Abu Dhabi Bank\n', '330.32\n']
     Rank                      Bank Name Total Assets 2025($)
0     2\n   Agricultural Bank of China\n           5,923.76\n
1     3\n      China Construction Bank\n           5,558.38\n
2     4\n                Bank of China\n           4,803.51\n
3     5\n               JPMorgan Chase\n           4,002.81\n
4     6\n              Bank of America\n           3,261.52\n
..    ...                            ...                  ...
94   96\n                    SEB Group\n             339.65\n
95   97\n             Raiffeisen Group\n             337.25\n
96   98\n               Banco Bradesco\n             331.96\n
97   99\n                     VTB Bank\n             330.43\n
98  100\n         First Abu Dhabi Bank\n             330.32\n

[99 rows x 3 columns]

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
['1\n']
['1\n', ' Industrial and Commercial Bank of China\n']
['1\n', ' Industrial and Commercial Bank of China\n', '6,688.74\n']
['2\n']
['2\n', ' Agricultural Bank of China\n']
['2\n', ' Agricultural Bank of China\n', '5,923.76\n']
['3\n']
['3\n', ' China Construction Bank\n']
['3\n', ' China Construction Bank\n', '5,558.38\n']
['4\n']
['4\n', ' Bank of China\n']
['4\n', ' Bank of China\n', '4,803.51\n']
['5\n']
['5\n', ' JPMorgan Chase\n']
['5\n', ' JPMorgan Chase\n', '4,002.81\n']
['6\n']
['6\n', ' Bank of America\n']
['6\n', ' Bank of America\n', '3,261.52\n']
['7\n']
['7\n', ' HSBC\n']
['7\n', ' HSBC\n', '2,989.81\n']
['8\n']
['8\n', ' BNP Paribas\n']
['8\n', ' BNP Paribas\n', '2,809.83\n']
['9\n']
['9\n', ' Crédit Agricole\n']
['9\n', ' Crédit Agricole\n', '2,693.58\n']
['10\n']
['10\n', ' Mitsubishi UFJ Financial Group\n']
['10\n', ' Mitsubishi UFJ Financial Group\n', '2,628.12\n']
['11\n']
['11\n', ' Postal Savings Bank of China\n']
['11\n', ' Postal Savings Bank of China\n', '2,340.69\n']
['12\n']
['12\n', ' Citigroup\n']
['12\n', ' Citigroup\n', '2,151.95\n']
['13\n']
['13\n', ' Bank of Communications\n']
['13\n', ' Bank of Communications\n', '2,041.45\n']
['14\n']
['14\n', ' SMBC Group\n']
['14\n', ' SMBC Group\n', '1,977.18\n']
['15\n']
['15\n', ' Wells Fargo\n']
['15\n', ' Wells Fargo\n', '1,929.85\n']
['16\n']
['16\n', ' Banco Santander\n']
['16\n', ' Banco Santander\n', '1,901.94\n']
['17\n']
['17\n', ' Barclays\n']
['17\n', ' Barclays\n', '1,900.67\n']
['18\n']
['18\n', ' Mizuho Financial Group\n']
['18\n', ' Mizuho Financial Group\n', '1,805.52\n']
['19\n']
['19\n', ' Goldman Sachs\n']
['19\n', ' Goldman Sachs\n', '1,675.97\n']
['20\n']
['20\n', ' China Merchants Bank\n']
['20\n', ' China Merchants Bank\n', '1,664.87\n']
['21\n']
['21\n', ' Groupe BPCE\n']
['21\n', ' Groupe BPCE\n', '1,646.53\n']
['22\n']
['22\n', ' Société Générale\n']
['22\n', ' Société Générale\n', '1,601.74\n']
['23\n']
['23\n', ' UBS\n']
['23\n', ' UBS\n', '1,563.32\n']
['24\n']
['24\n', ' Japan Post Bank\n']
['24\n', ' Japan Post Bank\n', '1,546.95\n']
['25\n']
['25\n', ' Royal Bank of Canada\n']
['25\n', ' Royal Bank of Canada\n', '1,513.86\n']
['26\n']
['26\n', ' Toronto-Dominion Bank\n']
['26\n', ' Toronto-Dominion Bank\n', '1,446.51\n']
['27\n']
['27\n', ' Industrial Bank\n']
['27\n', ' Industrial Bank\n', '1,439.62\n']
['28\n']
['28\n', ' Deutsche Bank\n']
['28\n', ' Deutsche Bank\n', '1,436.15\n']
['29\n']
['29\n', ' China CITIC Bank\n']
['29\n', ' China CITIC Bank\n', '1,306.01\n']
['30\n']
['30\n', ' Shanghai Pudong Development Bank\n']
['30\n', ' Shanghai Pudong Development Bank\n', '1,296.31\n']
['31\n']
['31\n', ' Crédit Mutuel\n']
['31\n', ' Crédit Mutuel\n', '1,252.10\n']
['32\n']
['32\n', ' Morgan Stanley\n']
['32\n', ' Morgan Stanley\n', '1,215.07\n']
['33\n']
['33\n', ' Lloyds Banking Group\n']
['33\n', ' Lloyds Banking Group\n', '1,135.12\n']
['34\n']
['34\n', ' China Minsheng Bank\n']
['34\n', ' China Minsheng Bank\n', '1,070.68\n']
['35\n']
['35\n', ' ING Group\n']
['35\n', ' ING Group\n', '1,056.57\n']
['36\n']
['36\n', ' Bank of Montreal\n']
['36\n', ' Bank of Montreal\n', '1,014.36\n']
['37\n']
['37\n', ' Scotiabank\n']
['37\n', ' Scotiabank\n', '978.47\n']
['38\n']
['38\n', ' Intesa Sanpaolo\n']
['38\n', ' Intesa Sanpaolo\n', '966.23\n']
['39\n']
['39\n', ' China Everbright Bank\n']
['39\n', ' China Everbright Bank\n', '953.41\n']
['40\n']
['40\n', ' NatWest Group\n']
['40\n', ' NatWest Group\n', '886.34\n']
['41\n']
['41\n', ' ANZ Group\n']
['41\n', ' ANZ Group\n', '852.19\n']
['42\n']
['42\n', ' Standard Chartered\n']
['42\n', ' Standard Chartered\n', '849.69\n']
['43\n']
['43\n', ' State Bank of India\n']
['43\n', ' State Bank of India\n', '846.64\n']
['44\n']
['44\n', ' UniCredit\n']
['44\n', ' UniCredit\n', '811.68\n']
['45\n']
['45\n', ' Commonwealth Bank\n']
['45\n', ' Commonwealth Bank\n', '809.81\n']
['46\n']
['46\n', ' Banco Bilbao Vizcaya Argentaria\n']
['46\n', ' Banco Bilbao Vizcaya Argentaria\n', '799.67\n']
['47\n']
['47\n', ' Ping An Bank\n']
['47\n', ' Ping An Bank\n', '790.41\n']
['48\n']
['48\n', ' La Banque postale\n']
['48\n', ' La Banque postale\n', '766.91\n']
['49\n']
['49\n', ' National Australia Bank\n']
['49\n', ' National Australia Bank\n', '748.98\n']
['50\n']
['50\n', ' Canadian Imperial Bank of Commerce\n']
['50\n', ' Canadian Imperial Bank of Commerce\n', '747.91\n']
['51\n']
['51\n', ' Westpac\n']
['51\n', ' Westpac\n', '747.10\n']
['52\n']
['52\n', ' DZ Bank\n']
['52\n', ' DZ Bank\n', '682.93\n']
['53\n']
['53\n', ' U.S. Bancorp\n']
['53\n', ' U.S. Bancorp\n', '678.32\n']
['54\n']
['54\n', ' CaixaBank\n']
['54\n', ' CaixaBank\n', '653.28\n']
['55\n']
['55\n', ' Rabobank\n']
['55\n', ' Rabobank\n', '651.47\n']
['56\n']
['56\n', ' Nordea\n']
['56\n', ' Nordea\n', '645.36\n']
['57\n']
['57\n', ' Capital One\n']
['57\n', ' Capital One\n', '637.78\n']
['58\n']
['58\n', ' DBS Group\n']
['58\n', ' DBS Group\n', '606.13\n']
['59\n']
['59\n', ' Huaxia Bank\n']
['59\n', ' Huaxia Bank\n', '599.59\n']
['60\n']
['60\n', ' Commerzbank\n']
['60\n', ' Commerzbank\n', '574.23\n']
['61\n']
['61\n', ' Bank of Beijing\n']
['61\n', ' Bank of Beijing\n', '574.14\n']
['62\n']
['62\n', ' Norinchukin Bank\n']
['62\n', ' Norinchukin Bank\n', '560.75\n']
['63\n']
['63\n', ' PNC Financial Services\n']
['63\n', ' PNC Financial Services\n', '560.04\n']
['64\n']
['64\n', ' Sberbank of Russia\n']
['64\n', ' Sberbank of Russia\n', '557.48\n']
['65\n']
['65\n', ' Bank of Jiangsu\n']
['65\n', ' Bank of Jiangsu\n', '541.41\n']
['66\n']
['66\n', ' Truist Financial Corp\n']
['66\n', ' Truist Financial Corp\n', '531.18\n']
['67\n']
['67\n', ' Danske Bank\n']
['67\n', ' Danske Bank\n', '515.87\n']
['68\n']
['68\n', ' KB Financial Group\n']
['68\n', ' KB Financial Group\n', '513.01\n']
['69\n']
['69\n', ' Shinhan Financial Group\n']
['69\n', ' Shinhan Financial Group\n', '500.77\n']
['70\n']
['70\n', ' Nationwide Building Society\n']
['70\n', ' Nationwide Building Society\n', '498.77\n']
['71\n']
['71\n', ' Sumitomo Mitsui Trust Holdings\n']
['71\n', ' Sumitomo Mitsui Trust Holdings\n', '498.16\n']
['72\n']
['72\n', ' China Guangfa Bank\n']
['72\n', ' China Guangfa Bank\n', '494.93\n']
['73\n']
['73\n', ' HDFC Bank\n']
['73\n', ' HDFC Bank\n', '494.06\n']
['74\n']
['74\n', ' Itaú Unibanco\n']
['74\n', ' Itaú Unibanco\n', '492.90\n']
['75\n']
['75\n', ' Resona Holdings\n']
['75\n', ' Resona Holdings\n', '491.13\n']
['76\n']
['76\n', ' Charles Schwab Corporation\n']
['76\n', ' Charles Schwab Corporation\n', '479.84\n']
['77\n']
['77\n', ' Oversea-Chinese Banking Corporation\n']
['77\n', ' Oversea-Chinese Banking Corporation\n', '458.00\n']
['78\n']
['78\n', ' China Zheshang Bank\n']
['78\n', ' China Zheshang Bank\n', '455.61\n']
['79\n']
['79\n', ' Bank of Shanghai\n']
['79\n', ' Bank of Shanghai\n', '442.06\n']
['80\n']
['80\n', ' Hana Financial Group\n']
['80\n', ' Hana Financial Group\n', '431.78\n']
['81\n']
['81\n', ' Bank of Ningbo\n']
['81\n', ' Bank of Ningbo\n', '428.16\n']
['82\n']
['82\n', ' Nonghyup Bank\n']
['82\n', ' Nonghyup Bank\n', '419.37\n']
['83\n']
['83\n', ' BNY Mellon\n']
['83\n', ' BNY Mellon\n', '416.06\n']
['84\n']
['84\n', ' ABN AMRO\n']
['84\n', ' ABN AMRO\n', '411.66\n']
['85\n']
['85\n', ' United Overseas Bank\n']
['85\n', ' United Overseas Bank\n', '393.97\n']
['86\n']
['86\n', ' Banco do Brasil\n']
['86\n', ' Banco do Brasil\n', '393.52\n']
['87\n']
['87\n', ' Woori Financial Group\n']
['87\n', ' Woori Financial Group\n', '393.34\n']
['88\n']
['88\n', ' KBC Group\n']
['88\n', ' KBC Group\n', '386.22\n']
['89\n']
['89\n', ' Nomura Holdings\n']
['89\n', ' Nomura Holdings\n', '385.00\n']
['90\n']
['90\n', ' Landesbank Baden-Württemberg\n']
['90\n', ' Landesbank Baden-Württemberg\n', '368.98\n']
['91\n']
['91\n', ' Erste Group\n']
['91\n', ' Erste Group\n', '366.22\n']
['92\n']
['92\n', ' National Bank of Canada\n']
['92\n', ' National Bank of Canada\n', '365.25\n']
['93\n']
['93\n', ' State Street Corporation\n']
['93\n', ' State Street Corporation\n', '362.95\n']
['94\n']
['94\n', ' Qatar National Bank\n']
['94\n', ' Qatar National Bank\n', '356.52\n']
['95\n']
['95\n', ' Bank of Nanjing\n']
['95\n', ' Bank of Nanjing\n', '355.03\n']
['96\n']
['96\n', ' SEB Group\n']
['96\n', ' SEB Group\n', '339.65\n']
['97\n']
['97\n', ' Raiffeisen Group\n']
['97\n', ' Raiffeisen Group\n', '337.25\n']
['98\n']
['98\n', ' Banco Bradesco\n']
['98\n', ' Banco Bradesco\n', '331.96\n']
['99\n']
['99\n', ' VTB Bank\n']
['99\n', ' VTB Bank\n', '330.43\n']
['100\n']
['100\n', ' First Abu Dhabi Bank\n']
['100\n', ' First Abu Dhabi Bank\n', '330.32\n']
     Rank                                   Bank Name Total Assets 2025($)
0     1\n   Industrial and Commercial Bank of China\n           6,688.74\n
1     2\n                Agricultural Bank of China\n           5,923.76\n
2     3\n                   China Construction Bank\n           5,558.38\n
3     4\n                             Bank of China\n           4,803.51\n
4     5\n                            JPMorgan Chase\n           4,002.81\n
..    ...                                         ...                  ...
95   96\n                                 SEB Group\n             339.65\n
96   97\n                          Raiffeisen Group\n             337.25\n
97   98\n                            Banco Bradesco\n             331.96\n
98   99\n                                  VTB Bank\n             330.43\n
99  100\n                      First Abu Dhabi Bank\n             330.32\n

[100 rows x 3 columns]
Transforming process started..
Data Transformed Successfully..
Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 78, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 73, in main
    print(transforemd_data_frame)
NameError: name 'transforemd_data_frame' is not defined. Did you mean: 'transformed_data_frame'?

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 79, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 61, in main
    for row in soup_table[0,5]:
TypeError: tuple indices must be integers or slices, not tuple

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
['1\n']
['1\n', ' Industrial and Commercial Bank of China\n']
['1\n', ' Industrial and Commercial Bank of China\n', '6,688.74\n']
['2\n']
['2\n', ' Agricultural Bank of China\n']
['2\n', ' Agricultural Bank of China\n', '5,923.76\n']
['3\n']
['3\n', ' China Construction Bank\n']
['3\n', ' China Construction Bank\n', '5,558.38\n']
['4\n']
['4\n', ' Bank of China\n']
['4\n', ' Bank of China\n', '4,803.51\n']
['5\n']
['5\n', ' JPMorgan Chase\n']
['5\n', ' JPMorgan Chase\n', '4,002.81\n']
  Rank                                   Bank Name Total Assets 2025($)
0  1\n   Industrial and Commercial Bank of China\n           6,688.74\n
1  2\n                Agricultural Bank of China\n           5,923.76\n
2  3\n                   China Construction Bank\n           5,558.38\n
3  4\n                             Bank of China\n           4,803.51\n
4  5\n                            JPMorgan Chase\n           4,002.81\n
Transforming process started..
Data Transformed Successfully..
   Rank  ... Toatal Assets in INR
0     1  ...            603591.90
1     2  ...            534560.10
2     3  ...            501588.21
3     4  ...            433468.74
4     5  ...            361213.57

[5 rows x 6 columns]

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
  Rank                                   Bank Name Total Assets 2025($)
0  1\n   Industrial and Commercial Bank of China\n           6,688.74\n
1  2\n                Agricultural Bank of China\n           5,923.76\n
2  3\n                   China Construction Bank\n           5,558.38\n
3  4\n                             Bank of China\n           4,803.51\n
4  5\n                            JPMorgan Chase\n           4,002.81\n
Transforming process started..
Data Transformed Successfully..
   Rank  ... Toatal Assets in INR
0     1  ...            603591.90
1     2  ...            534560.10
2     3  ...            501588.21
3     4  ...            433468.74
4     5  ...            361213.57

[5 rows x 6 columns]

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
   Rank  ... Toatal Assets in INR
0     1  ...            603591.90
1     2  ...            534560.10
2     3  ...            501588.21
3     4  ...            433468.74
4     5  ...            361213.57

[5 rows x 6 columns]

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
   Rank  ... Toatal Assets in INR
0     1  ...            603591.90
1     2  ...            534560.10
2     3  ...            501588.21

[3 rows x 6 columns]

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
Traceback (most recent call last):
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexes\base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 79, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 74, in main
    print(transformed_data_frame.loc[0,0],transformed_data_frame.loc[0,1],transformed_data_frame.loc[0,2], transformed_data_frame.loc[0,3], transformed_data_frame.loc[0,4], transformed_data_frame.loc[0,5])
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 1183, in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
  File "E:\Python(latest)\Lib\site-packages\pandas\core\frame.py", line 4214, in _get_value
    series = self._get_item_cache(col)
  File "E:\Python(latest)\Lib\site-packages\pandas\core\frame.py", line 4638, in _get_item_cache
    loc = self.columns.get_loc(item)
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 0

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 79, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 74, in main
    print(transformed_data_frame.get_loc[0,0],transformed_data_frame.get_loc[0,1],transformed_data_frame.get_loc[0,2], transformed_data_frame.get_loc[0,3], transformed_data_frame.get_loc[0,4], transformed_data_frame.get_loc[0,5])
  File "E:\Python(latest)\Lib\site-packages\pandas\core\generic.py", line 6299, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'get_loc'

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 79, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 74, in main
    print(transformed_data_frame.get_loc[0])
  File "E:\Python(latest)\Lib\site-packages\pandas\core\generic.py", line 6299, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'get_loc'

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 79, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 74, in main
    print(transformed_data_frame.iat[0:1])
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 2526, in __getitem__
    key = self._convert_key(key)
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 2599, in _convert_key
    raise ValueError("iAt based indexing can only have integer indexers")
ValueError: iAt based indexing can only have integer indexers

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 79, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 74, in main
    print(transformed_data_frame.iat[0])
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexing.py", line 2527, in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
TypeError: DataFrame._get_value() missing 1 required positional argument: 'col'

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
1

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 102, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 97, in main
    print(loading(transformed_data_frame))
NameError: name 'loading' is not defined. Did you mean: 'loding'?

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
Started loading process..
CSV file creted successfully
Table created in DB successfully
None

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
Started loading process..
CSV file creted successfully
Table created in DB successfully
True

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 132, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 120, in main
    transformed_data_frame = transform(table_data_frame, col, variation )
  File "E:/Data Engineer/projects/world_bank_practice.py", line 50, in transform
    logging('transform')
  File "E:/Data Engineer/projects/world_bank_practice.py", line 82, in logging
    f.write(datetime.now()+ ' : Data Transformed and returned a DataFrame.')
TypeError: unsupported operand type(s) for +: 'datetime.datetime' and 'str'
datetime.now()
datetime.datetime(2025, 12, 3, 13, 8, 12, 576072)
str(datetime.now())
'2025-12-03 13:09:20.627521'

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..
Logged Exection Detaails successfully..
Started loading process..
CSV file creted successfully..
Table created in DB successfully..
Logged Exection Detaails successfully..
True

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..

Logged Exection Details successfully..

Started loading process..
CSV file creted successfully..
Table created in DB successfully..

Logged Exection Details successfully..

True

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..

Logged Exection Details successfully..

Query executed successfully..
Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 145, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 141, in main
    print(querying(query, db_name))
  File "E:/Data Engineer/projects/world_bank_practice.py", line 104, in querying
    logging('query')
  File "E:/Data Engineer/projects/world_bank_practice.py", line 89, in logging
    f.write(str(datetime.now())+ ' : Query Execution completed.')
UnboundLocalError: cannot access local variable 'f' where it is not associated with a value

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..

Logged Exection Details successfully..

Traceback (most recent call last):
  File "E:\Python(latest)\Lib\site-packages\pandas\io\sql.py", line 2674, in execute
    cur.execute(sql, *args)
sqlite3.OperationalError: near "10": syntax error

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 146, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 142, in main
    print(querying(query, db_name))
  File "E:/Data Engineer/projects/world_bank_practice.py", line 102, in querying
    ans = pd.read_sql(query, conn)
  File "E:\Python(latest)\Lib\site-packages\pandas\io\sql.py", line 706, in read_sql
    return pandas_sql.read_query(
  File "E:\Python(latest)\Lib\site-packages\pandas\io\sql.py", line 2738, in read_query
    cursor = self.execute(sql, params)
  File "E:\Python(latest)\Lib\site-packages\pandas\io\sql.py", line 2686, in execute
    raise ex from exc
pandas.errors.DatabaseError: Execution failed on sql 'select top 10 * from top_10_world_banks': near "10": syntax error

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..

Logged Exection Details successfully..

Traceback (most recent call last):
  File "E:\Python(latest)\Lib\site-packages\pandas\io\sql.py", line 2674, in execute
    cur.execute(sql, *args)
sqlite3.OperationalError: near "10": syntax error

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "E:/Data Engineer/projects/world_bank_practice.py", line 146, in <module>
    main()
  File "E:/Data Engineer/projects/world_bank_practice.py", line 142, in main
    print(querying(query, db_name))
  File "E:/Data Engineer/projects/world_bank_practice.py", line 102, in querying
    ans = pd.read_sql(query, conn)
  File "E:\Python(latest)\Lib\site-packages\pandas\io\sql.py", line 706, in read_sql
    return pandas_sql.read_query(
  File "E:\Python(latest)\Lib\site-packages\pandas\io\sql.py", line 2738, in read_query
    cursor = self.execute(sql, params)
  File "E:\Python(latest)\Lib\site-packages\pandas\io\sql.py", line 2686, in execute
    raise ex from exc
pandas.errors.DatabaseError: Execution failed on sql 'select * from top_10_world_bankslimit 10': near "10": syntax error

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..

Logged Exection Details successfully..

Query executed successfully..

Logged Exection Details successfully..

   Rank  ... Toatal Assets in INR
0     1  ...            603591.90
1     2  ...            534560.10
2     3  ...            501588.21
3     4  ...            433468.74
4     5  ...            361213.57

[5 rows x 6 columns]

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Transforming process started..
Data Transformed Successfully..

Logged Exection Details successfully..

Query executed successfully..

Logged Exection Details successfully..

   Rank  ... Toatal Assets in INR
0     1  ...            603591.90
1     2  ...            534560.10
2     3  ...            501588.21
3     4  ...            433468.74
4     5  ...            361213.57

[5 rows x 6 columns]

=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Started Extraction of data..

['1\n']
['1\n', ' Industrial and Commercial Bank of China\n']
['1\n', ' Industrial and Commercial Bank of China\n', '6,688.74\n']
['2\n']
['2\n', ' Agricultural Bank of China\n']
['2\n', ' Agricultural Bank of China\n', '5,923.76\n']
['3\n']
['3\n', ' China Construction Bank\n']
['3\n', ' China Construction Bank\n', '5,558.38\n']
['4\n']
['4\n', ' Bank of China\n']
['4\n', ' Bank of China\n', '4,803.51\n']
['5\n']
['5\n', ' JPMorgan Chase\n']
['5\n', ' JPMorgan Chase\n', '4,002.81\n']
['6\n']
['6\n', ' Bank of America\n']
['6\n', ' Bank of America\n', '3,261.52\n']
['7\n']
['7\n', ' HSBC\n']
['7\n', ' HSBC\n', '2,989.81\n']
['8\n']
['8\n', ' BNP Paribas\n']
['8\n', ' BNP Paribas\n', '2,809.83\n']
['9\n']
['9\n', ' Crédit Agricole\n']
['9\n', ' Crédit Agricole\n', '2,693.58\n']
['10\n']
['10\n', ' Mitsubishi UFJ Financial Group\n']
['10\n', ' Mitsubishi UFJ Financial Group\n', '2,628.12\n']
['11\n']
['11\n', ' Postal Savings Bank of China\n']
['11\n', ' Postal Savings Bank of China\n', '2,340.69\n']
['12\n']
['12\n', ' Citigroup\n']
['12\n', ' Citigroup\n', '2,151.95\n']
['13\n']
['13\n', ' Bank of Communications\n']
['13\n', ' Bank of Communications\n', '2,041.45\n']
['14\n']
['14\n', ' SMBC Group\n']
['14\n', ' SMBC Group\n', '1,977.18\n']
['15\n']
['15\n', ' Wells Fargo\n']
['15\n', ' Wells Fargo\n', '1,929.85\n']
['16\n']
['16\n', ' Banco Santander\n']
['16\n', ' Banco Santander\n', '1,901.94\n']
['17\n']
['17\n', ' Barclays\n']
['17\n', ' Barclays\n', '1,900.67\n']
['18\n']
['18\n', ' Mizuho Financial Group\n']
['18\n', ' Mizuho Financial Group\n', '1,805.52\n']
['19\n']
['19\n', ' Goldman Sachs\n']
['19\n', ' Goldman Sachs\n', '1,675.97\n']
['20\n']
['20\n', ' China Merchants Bank\n']
['20\n', ' China Merchants Bank\n', '1,664.87\n']
['21\n']
['21\n', ' Groupe BPCE\n']
['21\n', ' Groupe BPCE\n', '1,646.53\n']
['22\n']
['22\n', ' Société Générale\n']
['22\n', ' Société Générale\n', '1,601.74\n']
['23\n']
['23\n', ' UBS\n']
['23\n', ' UBS\n', '1,563.32\n']
['24\n']
['24\n', ' Japan Post Bank\n']
['24\n', ' Japan Post Bank\n', '1,546.95\n']
['25\n']
['25\n', ' Royal Bank of Canada\n']
['25\n', ' Royal Bank of Canada\n', '1,513.86\n']
['26\n']
['26\n', ' Toronto-Dominion Bank\n']
['26\n', ' Toronto-Dominion Bank\n', '1,446.51\n']
['27\n']
['27\n', ' Industrial Bank\n']
['27\n', ' Industrial Bank\n', '1,439.62\n']
['28\n']
['28\n', ' Deutsche Bank\n']
['28\n', ' Deutsche Bank\n', '1,436.15\n']
['29\n']
['29\n', ' China CITIC Bank\n']
['29\n', ' China CITIC Bank\n', '1,306.01\n']
['30\n']
['30\n', ' Shanghai Pudong Development Bank\n']
['30\n', ' Shanghai Pudong Development Bank\n', '1,296.31\n']
['31\n']
['31\n', ' Crédit Mutuel\n']
['31\n', ' Crédit Mutuel\n', '1,252.10\n']
['32\n']
['32\n', ' Morgan Stanley\n']
['32\n', ' Morgan Stanley\n', '1,215.07\n']
['33\n']
['33\n', ' Lloyds Banking Group\n']
['33\n', ' Lloyds Banking Group\n', '1,135.12\n']
['34\n']
['34\n', ' China Minsheng Bank\n']
['34\n', ' China Minsheng Bank\n', '1,070.68\n']
['35\n']
['35\n', ' ING Group\n']
['35\n', ' ING Group\n', '1,056.57\n']
['36\n']
['36\n', ' Bank of Montreal\n']
['36\n', ' Bank of Montreal\n', '1,014.36\n']
['37\n']
['37\n', ' Scotiabank\n']
['37\n', ' Scotiabank\n', '978.47\n']
['38\n']
['38\n', ' Intesa Sanpaolo\n']
['38\n', ' Intesa Sanpaolo\n', '966.23\n']
['39\n']
['39\n', ' China Everbright Bank\n']
['39\n', ' China Everbright Bank\n', '953.41\n']
['40\n']
['40\n', ' NatWest Group\n']
['40\n', ' NatWest Group\n', '886.34\n']
['41\n']
['41\n', ' ANZ Group\n']
['41\n', ' ANZ Group\n', '852.19\n']
['42\n']
['42\n', ' Standard Chartered\n']
['42\n', ' Standard Chartered\n', '849.69\n']
['43\n']
['43\n', ' State Bank of India\n']
['43\n', ' State Bank of India\n', '846.64\n']
['44\n']
['44\n', ' UniCredit\n']
['44\n', ' UniCredit\n', '811.68\n']
['45\n']
['45\n', ' Commonwealth Bank\n']
['45\n', ' Commonwealth Bank\n', '809.81\n']
['46\n']
['46\n', ' Banco Bilbao Vizcaya Argentaria\n']
['46\n', ' Banco Bilbao Vizcaya Argentaria\n', '799.67\n']
['47\n']
['47\n', ' Ping An Bank\n']
['47\n', ' Ping An Bank\n', '790.41\n']
['48\n']
['48\n', ' La Banque postale\n']
['48\n', ' La Banque postale\n', '766.91\n']
['49\n']
['49\n', ' National Australia Bank\n']
['49\n', ' National Australia Bank\n', '748.98\n']
['50\n']
['50\n', ' Canadian Imperial Bank of Commerce\n']
['50\n', ' Canadian Imperial Bank of Commerce\n', '747.91\n']
['51\n']
['51\n', ' Westpac\n']
['51\n', ' Westpac\n', '747.10\n']
['52\n']
['52\n', ' DZ Bank\n']
['52\n', ' DZ Bank\n', '682.93\n']
['53\n']
['53\n', ' U.S. Bancorp\n']
['53\n', ' U.S. Bancorp\n', '678.32\n']
['54\n']
['54\n', ' CaixaBank\n']
['54\n', ' CaixaBank\n', '653.28\n']
['55\n']
['55\n', ' Rabobank\n']
['55\n', ' Rabobank\n', '651.47\n']
['56\n']
['56\n', ' Nordea\n']
['56\n', ' Nordea\n', '645.36\n']
['57\n']
['57\n', ' Capital One\n']
['57\n', ' Capital One\n', '637.78\n']
['58\n']
['58\n', ' DBS Group\n']
['58\n', ' DBS Group\n', '606.13\n']
['59\n']
['59\n', ' Huaxia Bank\n']
['59\n', ' Huaxia Bank\n', '599.59\n']
['60\n']
['60\n', ' Commerzbank\n']
['60\n', ' Commerzbank\n', '574.23\n']
['61\n']
['61\n', ' Bank of Beijing\n']
['61\n', ' Bank of Beijing\n', '574.14\n']
['62\n']
['62\n', ' Norinchukin Bank\n']
['62\n', ' Norinchukin Bank\n', '560.75\n']
['63\n']
['63\n', ' PNC Financial Services\n']
['63\n', ' PNC Financial Services\n', '560.04\n']
['64\n']
['64\n', ' Sberbank of Russia\n']
['64\n', ' Sberbank of Russia\n', '557.48\n']
['65\n']
['65\n', ' Bank of Jiangsu\n']
['65\n', ' Bank of Jiangsu\n', '541.41\n']
['66\n']
['66\n', ' Truist Financial Corp\n']
['66\n', ' Truist Financial Corp\n', '531.18\n']
['67\n']
['67\n', ' Danske Bank\n']
['67\n', ' Danske Bank\n', '515.87\n']
['68\n']
['68\n', ' KB Financial Group\n']
['68\n', ' KB Financial Group\n', '513.01\n']
['69\n']
['69\n', ' Shinhan Financial Group\n']
['69\n', ' Shinhan Financial Group\n', '500.77\n']
['70\n']
['70\n', ' Nationwide Building Society\n']
['70\n', ' Nationwide Building Society\n', '498.77\n']
['71\n']
['71\n', ' Sumitomo Mitsui Trust Holdings\n']
['71\n', ' Sumitomo Mitsui Trust Holdings\n', '498.16\n']
['72\n']
['72\n', ' China Guangfa Bank\n']
['72\n', ' China Guangfa Bank\n', '494.93\n']
['73\n']
['73\n', ' HDFC Bank\n']
['73\n', ' HDFC Bank\n', '494.06\n']
['74\n']
['74\n', ' Itaú Unibanco\n']
['74\n', ' Itaú Unibanco\n', '492.90\n']
['75\n']
['75\n', ' Resona Holdings\n']
['75\n', ' Resona Holdings\n', '491.13\n']
['76\n']
['76\n', ' Charles Schwab Corporation\n']
['76\n', ' Charles Schwab Corporation\n', '479.84\n']
['77\n']
['77\n', ' Oversea-Chinese Banking Corporation\n']
['77\n', ' Oversea-Chinese Banking Corporation\n', '458.00\n']
['78\n']
['78\n', ' China Zheshang Bank\n']
['78\n', ' China Zheshang Bank\n', '455.61\n']
['79\n']
['79\n', ' Bank of Shanghai\n']
['79\n', ' Bank of Shanghai\n', '442.06\n']
['80\n']
['80\n', ' Hana Financial Group\n']
['80\n', ' Hana Financial Group\n', '431.78\n']
['81\n']
['81\n', ' Bank of Ningbo\n']
['81\n', ' Bank of Ningbo\n', '428.16\n']
['82\n']
['82\n', ' Nonghyup Bank\n']
['82\n', ' Nonghyup Bank\n', '419.37\n']
['83\n']
['83\n', ' BNY Mellon\n']
['83\n', ' BNY Mellon\n', '416.06\n']
['84\n']
['84\n', ' ABN AMRO\n']
['84\n', ' ABN AMRO\n', '411.66\n']
['85\n']
['85\n', ' United Overseas Bank\n']
['85\n', ' United Overseas Bank\n', '393.97\n']
['86\n']
['86\n', ' Banco do Brasil\n']
['86\n', ' Banco do Brasil\n', '393.52\n']
['87\n']
['87\n', ' Woori Financial Group\n']
['87\n', ' Woori Financial Group\n', '393.34\n']
['88\n']
['88\n', ' KBC Group\n']
['88\n', ' KBC Group\n', '386.22\n']
['89\n']
['89\n', ' Nomura Holdings\n']
['89\n', ' Nomura Holdings\n', '385.00\n']
['90\n']
['90\n', ' Landesbank Baden-Württemberg\n']
['90\n', ' Landesbank Baden-Württemberg\n', '368.98\n']
['91\n']
['91\n', ' Erste Group\n']
['91\n', ' Erste Group\n', '366.22\n']
['92\n']
['92\n', ' National Bank of Canada\n']
['92\n', ' National Bank of Canada\n', '365.25\n']
['93\n']
['93\n', ' State Street Corporation\n']
['93\n', ' State Street Corporation\n', '362.95\n']
['94\n']
['94\n', ' Qatar National Bank\n']
['94\n', ' Qatar National Bank\n', '356.52\n']
['95\n']
['95\n', ' Bank of Nanjing\n']
['95\n', ' Bank of Nanjing\n', '355.03\n']
['96\n']
['96\n', ' SEB Group\n']
['96\n', ' SEB Group\n', '339.65\n']
['97\n']
['97\n', ' Raiffeisen Group\n']
['97\n', ' Raiffeisen Group\n', '337.25\n']
['98\n']
['98\n', ' Banco Bradesco\n']
['98\n', ' Banco Bradesco\n', '331.96\n']
['99\n']
['99\n', ' VTB Bank\n']
['99\n', ' VTB Bank\n', '330.43\n']
['100\n']
['100\n', ' First Abu Dhabi Bank\n']
['100\n', ' First Abu Dhabi Bank\n', '330.32\n']
Data frame creation Successful..

Logged Exection Details successfully..

Transforming process started..
Data Transformed Successfully..

Logged Exection Details successfully..

Started loading process..
CSV file creted successfully..
Table created in DB successfully..

Logged Exection Details successfully..

True
Query executed successfully..

Logged Exection Details successfully..

   Rank  ... Toatal Assets in INR
0     1  ...            603591.90
1     2  ...            534560.10
2     3  ...            501588.21
3     4  ...            433468.74
4     5  ...            361213.57
5     6  ...            294319.56
6     7  ...            269800.45
7     8  ...            253559.06
8     9  ...            243068.66
9    10  ...            237161.55

[10 rows x 6 columns]
*****Completed*****
>>> 
=========== RESTART: E:/Data Engineer/projects/world_bank_practice.py ==========
Started Extraction of data..
Data frame creation Successful..

Logged Exection Details successfully..

Transforming process started..
Data Transformed Successfully..

Logged Exection Details successfully..

Started loading process..
CSV file creted successfully..
Table created in DB successfully..

Logged Exection Details successfully..

True
Query executed successfully..

Logged Exection Details successfully..

   Rank  ... Toatal Assets in INR
0     1  ...            603591.90
1     2  ...            534560.10
2     3  ...            501588.21
3     4  ...            433468.74
4     5  ...            361213.57
5     6  ...            294319.56
6     7  ...            269800.45
7     8  ...            253559.06
8     9  ...            243068.66
9    10  ...            237161.55

[10 rows x 6 columns]
*****Completed*****
