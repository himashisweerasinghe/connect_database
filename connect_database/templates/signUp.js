{% if messg %}
<script>
    alert('{{messg}}');
</script>
{% endif %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sign-In</title>
</head>
<body>
<form action="/postsignup/" method="post">
    {% csrf_token %}
    Name :
    <input type="text" name="name"><br><br>
    Email :
    <input type="email" name="email"><br><br>

    Password :
    <input type="password" name="password"><br><br>
    <input type="submit" onclick="location.href='{% url 'signin' %}'" value="SignUp">

</form>
</body>
</html>