from sanic_requext import Form, FormField
from sanic import Sanic, response


app = Sanic(__name__)

class MyForm(Form):
    name = FormField()
    age = FormField()

@app.post("/form")
@MyForm.decorator
async def form(request, form):
    return response.text(f"hello, {form.name.value}! you are {form.age.value} years old")

app.run("0.0.0.0", 8080)