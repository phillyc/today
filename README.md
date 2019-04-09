# "Today" not "Todo"

## Prime directive

The guiding principal of this tool is the reduction of todos displayed each day.

The endless list is overwhelming and not usually useful, so care should be taken to only display a few tasks or even one at a time.

## Secondary goals

* Data you generate is yours, now and forever. Import and export should be stupidly easy.

* Laptops, cell phones, voice assistants, VR goggles, drones, etc, should all have the ability to push and pull from the app.

* Capture of a todo item should take less than 5 seconds.

* Todos should have a time estimate, time actual, date, place, and time of day. This is optional.

* Todos should be time and place sensitive. It's distracting to see house chores while you are in the office.

## Psychology

"The [Zeigarnik effect](https://en.wikipedia.org/wiki/Zeigarnik_effect) states that people remember uncompleted or interrupted tasks better than completed tasks."

While this particular effect has been disputed and hasn't been widely tested, it's fair to say that we want to keep the completed tasks *somewhere* for later review and analysis. In this way, we can complete tasks and forget about them, but be confident that we can recall and review them later.

"The [Ovsiankina effect](https://en.wikipedia.org/wiki/Ovsiankina_effect) is the tendency to pick up an interrupted action again when it has still not been achieved. ... It creates intrusive thoughts, aimed at taking up the task again."

It's obvious that the little things left undone eat away at us. This project aims to provide a way to "interupt" a task, then quickly get back on track when possible.


## Local Setup

Can use any Python version greater than 3.4.x

We're using django-heroku so make sure pipenv is installed and updated.

To initialize the virtualenv, from inside the /today directory, run `pipenv shell`.

You should see the (today) env on the prompt line.
