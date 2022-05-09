<!--Category:SQL,Powershell--> 
 <p align="right">
  <a href="https://www.powershellgallery.com/packages/ProductivityTools.SQLServerColumnDescription/"><img src="Images/Header/Powershell_border_40px.png" /></a>
    <a href="http://productivitytools.tech/sql-server-column-description/"><img src="Images/Header/ProductivityTools_green_40px_2.png" /><a> 
    <a href="https://github.com/pwujczyk/ProductivityTools.SQLServerColumnDescription"><img src="Images/Header/Github_border_40px.png" /></a>
</p>
<p align="center">
    <a href="http://http://productivitytools.tech/">
        <img src="Images/Header/LogoTitle_green_500px.png" />
    </a>
</p>



# Learning GCP FlaskWithFireStore

I am using [tutorial](https://medium.com/google-cloud/building-a-flask-python-crud-api-with-cloud-firestore-firebase-and-deploying-on-cloud-run-29a10c502877)

Project in firebase: **PTFlaskWithFirebase** I placed database in europe-west2

Requests
```
Invoke-WebRequest -Uri http://127.0.0.1:8080/list
```

```
Invoke-WebRequest -Uri http://127.0.0.1:8080/add -Method Post -Body (@{id='1';X='x1'}|ConvertTo-Json) -ContentType application/json
```