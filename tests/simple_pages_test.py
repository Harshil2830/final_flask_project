def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data
    assert b'href="/welcome"' in response.data
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index" in response.data


def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data


def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/welcome")
    assert response.status_code == 200
    assert b"welcome" in response.data
    assert b"Hi! I'm Harshil" in response.data
    assert b"I am a senior at NJIT graduating this semester majoring in IT specializing in Network and Information Security and minor in CS. GPA: 3.90" in response.data
    assert b"I work part-time at a small computer store as a Junior IT Service Specialist. I have a great deal of experience with Full-Stack development." in response.data
    assert b"Skills: <br> PHP, Python, JavaScript, HTML, CSS, Bootstrap, Java, Bash, C#, C++, SQL, MySQL, Data Structures and Algorithms, Object-Oriented Programming, Docker, Agile, Scrum, AWS, GIT, Linux" in response.data
    assert b"My Technologies" in response.data


def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Git" in response.data
    assert b"What are Branches?" in response.data
    assert b"What is a Merge?" in response.data
    assert b"What is a Commit?" in response.data
    assert b"What are Tags?" in response.data
    assert b"What are Repositories?" in response.data


def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Docker" in response.data
    assert b"What is a Docker Container and an Image?" in response.data
    assert b"How to get started" in response.data
    assert b"Some useful docker commands" in response.data
    assert b"This is a link to the docker repository of this website." in response.data


def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Flask" in response.data


def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"CI/CD" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
