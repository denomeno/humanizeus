print('''
<style>

ul {
list-style-type: none;
margin: 0;
padding: 0;
overflow: hidden;
background-color: #333;
}

li {
float: left;
}

li a {
display: block;
color: white;
text-align: center;
padding: 14px 16px;
text-decoration: none;
}

li a:hover {
background-color: #111;
}
</style>
''')


print('''
<ul>
    <li><a href='/humanizeus/home.py'><span>Home</span></a></li>
    <li><a href='/humanizeus/mission.py'><span>Our Mission</span></a></li>
    <li><a href='/humanizeus/map.py'><span>Map</span></a></li>
    <li><a href='/humanizeus/add_need.py'><span>Add Need</span></a></li>
    <li><a href='/humanizeus/add_support.py'><span>Add Support</span></a></li>
    <li><a href='/humanizeus/for_organizations.py'><span>For Organizations</span></a></li>
    <li><a href='/humanizeus/contact.py'><span>Contact Us</span></a></li>
</ul>
<br>
''')
