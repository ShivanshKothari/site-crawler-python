
<h1>Site Crawler</h1>

<p>Site Crawler is a simple web crawler built in Python for crawling web pages and extracting links.</p>

<h2>Overview</h2>

<p>The project consists of the following files:</p>

<ul>
  <li><strong>main.py</strong>: Initiates the web crawling process.</li>
  <li><strong>domain.py</strong>: Extracts domain and subdomain names.</li>
  <li><strong>general.py</strong>: Utility functions for file operations.</li>
  <li><strong>link_finder.py</strong>: Extracts links from HTML pages.</li>
  <li><strong>spider.py</strong>: Manages the crawling process.</li>
</ul>

<h2>Getting Started</h2>

<ol>
  <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/ShivanshKothari/site-crawler-python/
cd Site-Crawler
</code></pre>

<ol start="2">
  <li>Run the crawler:</li>
</ol>

<pre><code>python main.py
</code></pre>

<h2>Configuration</h2>

<ul>
  <li><strong>PROJECT_NAME</strong>: Project name (default: 'PlayStation').</li>
  <li><strong>HOMEPAGE</strong>: Starting URL for crawling (default: 'https://www.playstation.com/en-in/').</li>
  <li><strong>NUMBER_OF_THREADS</strong>: Number of threads for concurrent crawling (default: 6).</li>
</ul>

<h2>Usage</h2>

<p>The crawler starts from the provided homepage, follows links, and stores crawled and queued links in 'crawled.txt' and 'queue.txt', respectively.</p>

<h2>License</h2>

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

<p>Feel free to explore and customize the code for your web crawling needs!</p>
