<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
      div{
          position: absolute;
          right: 10px;
          top: 5px;
      }
    </style>
</head>
<body>
<div>
<button type="button" onclick="location.href='{% url 'log' %}'">Logout</button>
    </div>

Welcome {{e}}

<button type="button" onclick="location.href='{% url 'order' %}'">Go Eats</button>
</body>
</html>