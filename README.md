## Django shop

### Description
<p>Shop on Django>

### What it can do
<ul>
<li>retrieve products from the database and display them on templates</li>
<li>product search and filtering</li>
<li>save your purchases at Mongo</li>
<li>filling the basket in the session</li>
<li>authorization</li>
</ul>

### Available endpoints

<p><code>/search/</code> - search page (search on categories and price range); </p>
<p><code>/category/</code> - show all avaliable categories(used buttons); </p>
<p><code>/category/: category</code> - show all goods for [category];</p>
<p><code>/basket/</code> - show all goods in basket; </p>
<p><code>/users/login/</code> - use form to login; </p>
<p><code>/users/logout/</code> - use button to logout; </p>
<p><code>/admin/</code> - admin panel; </p>


### How to use
<p><code>source [your_env_name]/bin/activate</code> - activate your virtualenv</p>
<p><code>python manage.py runserver</code> - run server on http://127.0.0.1:8000 </p>
