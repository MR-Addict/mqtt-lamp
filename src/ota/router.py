from phew import server
from phew.template import render_template


@server.route("/")
def route_index(request):
    return render_template("ota/public/index.html")


def ota_run():
    server.run()
