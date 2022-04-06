# README

Hello,

From the explanations about The Eye sample project, I understood that: There are some points that are left unclear. I am expected to solve them. For this reason, I designed the application as I understand it.

1- I installed Django Rest API (this was mentioned in my first email)

2- Whether there are sites (applications) belonging to different customers such as A, B, C, they generate events such as A, E1, E2, E3, these events take place in the S1 session, but other events can also occur in the S2 or S3 Session. Based on this, I defined the model under models.py like this. I have class names Applications and Events. There should have been Session, but I didn't define the Session class because it's an example.

3-I connected Models to the API with Serializer.py.

4- Since there are in-page events of applications, I decided that the best way is Javascript. After all, this is way of Google Analytics and Yandex Metrica work.

5- Accordingly, each application will access our API by performing post operations from within a Javascript file.

6- It is also possible to send the name of the server to use an Identifier while doing this, instead I defined a unique UUID. It does not have perfect security. I agree but I just did it like this to keep it simple. Other ways are also available. I defined UUID as primary key and Foreign Key in Event class for *as a limitation* for possible irrelevant requests.

7- In the Django application, I left ALLOWED_HOST fully open to test, but in a real application, only the domain names of the relevant machines should be defined here. So it will only allow Javascript to be sent from those machines.

8-As an example, I created a file named `client_application.html` and sent a sample request via Vue and its works.

9-I also wrote a simple DocString for 9-Classes as a documentation example

10- I've used virtualenv and freezed required packs there.

11-I've used **JsonField** within the Event Class to keeping different type of Payload within my model.

Best regards