# the_eye_challenge

A coding challenge application named as 'The eye'. 

# The Eye Readme (with Remarks)

## Story

You work in an organization that has multiple applications serving websites, but it's super hard to analyze user behavior in those, because you have no data.

In order to be able to analyze user behavior (pages that are being accessed, buttons that are being clicked, forms that are being submitted, etc..), your team realized you need a service that aggregates that data.

*Verdict: To detect user click or similar activities the API should be with Javascript like Google Analytics
or yandex API*

---------------------------------------
*Types of interaction*

- *Form submission*
- *Page access*
- *Button click*
---------------------------------------

You're building "The Eye", a service that will collect those events from these applications, to help your org making better data-driven decisions.


## Workflow

* We don't want you to be a code monkey, **some things will not be 100% clear - and that's intended. We want to understand your assumptions and approaches you've taken during the implementation** - if you have questions, don't hesitate to ask
* Your commit history matters, we want to know the steps you've taken throughout the process, make sure you don't commit everything at once
* In the README.md of your project, explain what conclusions you've made from the entities, constraints, requirements and use cases of this test

---------------------------------------
Conclusions about the entities, constraints, requirements, and use cases
(Initial)

- Entity: An model or object that will be defined in the project(for this case django-rest)
- Constraint: When I hear this term here are three options:
    - The *literal* constraints you have defined in the title 'Constraints & Requirements'
    - The  database *plain* constraints like foreign key
    - Django Model constraints like:

        ````
        class Event(models.Model):
            start_date = models.DatetimeField() 
            end_date = models.DatetimeField()

        class Meta:
            constraints = [
                # Ensures constraint on DB level, raises IntegrityError (500 on debug=False)
                CheckConstraint(
                    check=Q(end_date__gt=F('start_date')), name='check_start_date',
                ),
            ]
        ````
        In Django constraints, we have the option `CheckConstraint` that provides more options for check.

        Assumption: Our aim with constraints is **data integrity** if we are using them as django or db constraints

- Requirements: A condition or capability needed by our project to solve a problem or achieve an objective. 
- User cases: A requirements specification is necessary to describe precisely what the system needs to do, but it sometimes may be an awful tool for communication. This is where the use case fits in.
---------------------------------------

## Entities

```
Application
    |
    |
  Event ---- Session
```

* An Event has a category, a name and a payload of data (the payload can change according to which event an Application is sending)
* Different types of Events (identified by category + name) can have different validations for their payloads 
* An Event is associated to a Session + 
* Events in a Session should be sequential and ordered by the time they occurred +
* The Application sending events is responsible for generating the Session identifier +
* Applications should be recognized as "trusted clients" to "The Eye" +
* Appllications can send events for the same session +

Example of events:
```json
{
  "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
  "category": "page interaction",
  "name": "pageview",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/",
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}

{
  "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
  "category": "page interaction",
  "name": "cta click",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/",
    "element": "chat bubble"
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}

{
  "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
  "category": "form interaction",
  "name": "submit",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/",
    "form": {
      "first_name": "John",
      "last_name": "Doe"
    }
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}
```

## Constraints & Requirements

* "The Eye" will be receiving, in average, ~100 events/second, so consider not processing events in real time
* When Applications talk to "The Eye", make sure to not leave them hanging +
* Your models should have proper constraints to avoid race conditions when multiple events are being processed at the same time +
* It must be implemented in Python with Django.

---------------------------------------

QUESTION A: According to Gisela's email  *The client???s stack is Django, Django REST Framework*. Do we prefer Django or Django REST API? If we prefer Django REST API, As I understand for query operations we just provide an API interface rather than HTML templates and forms. Is that true?

QUESTION B: In the same e-mail, Giseala mentioned DB as Postgres however I cannot see it in README.md (in your Github gist) Should I use Postgres or embededd SQLite in Django for this challenge.

QUESTION C: I understand that my task just defining the Django Models(including relations) and setting some test data according to the requirements you defined. Is that true?

---------------------------------------

* Share a public github repository when you are done.

## Use cases:

**You don't need to implement these use cases, they just help you modelling the application**

* Your data & analytics team should be able to quickly query events from:
  * A specific session
  * A specific category
  * A specific time range

* Your team should be able to monitor errors that happen in "The Eye", for example:
  * An event that is sending an unexpected value in the payload +
  * An event that has an invalid timestamp (i.e.: future) +


## Pluses - if you wanna go beyond

* Your application is documented
* Your application is dockerized
* A reusable client that talks to "The Eye"
