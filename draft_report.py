from Gmail.create_draft import create_draft
from Pixela.api import get_all_counts
import sys

RECIPIENTS = [("CharlieBaylis1@gmail.com ", "Chez"),
              ("rmainland@netspace.net.au ", "Dad")]


def grade_total(total):
    grade_dict = {28: "A+", 27: "A+", 26: "A", 25: "A", 24: "B+", 23: "B+", 22: "B", 21: "B", 20: "C+",
                  19: "C+", 18: "C", 17: "C", 16: "D+", 15: "D+", 14: "D", 13: "D", 12: "E"}
    if grade_dict.get(total):
        return grade_dict.get(total)
    return "F"


def fill_html(recipient_name, grade, med, web, jrn, goal, total):
    return f"""<div dir="ltr">Hey {recipient_name},<div>Here's my accountability report for this week.</div>
    <div><br><b>Grade: {grade}</b></div>
    <div><br></div>
    <div>
        <table border="0" cellpadding="0" cellspacing="0" width="405" style="border-collapse:collapse;width:305pt">

            <colgroup>
                <col width="81" span="5" style="width:61pt">
            </colgroup>
            <tbody>
                <tr height="27" style="height:20pt">
                    <td height="27" width="81"
                        style="height:20pt;width:61pt;color:black;font-weight:700;text-align:center;vertical-align:middle;border:0.5pt solid windowtext;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                        Meditation</td>
                    <td width="81"
                        style="width:61pt;color:black;font-weight:700;text-align:center;vertical-align:middle;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:none;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                        Web Dev</td>
                    <td width="81"
                        style="width:61pt;color:black;font-weight:700;text-align:center;vertical-align:middle;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:none;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                        Journal</td>
                    <td width="81"
                        style="border-left:none;width:61pt;color:black;font-weight:700;text-align:center;vertical-align:middle;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                        Goal Research</td>
                    <td width="81"
                        style="border-left:none;width:61pt;color:black;font-weight:700;text-align:center;vertical-align:middle;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                        Total</td>
                </tr>
                <tr height="21" style="height:16pt">
                    <td height="21" width="81"
                        style="height:16pt;width:61pt;color:black;text-align:center;vertical-align:middle;border-top:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:0.5pt solid windowtext;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                        {med}/7</td>
                    <td width="81"
                        style="width:61pt;color:black;text-align:center;vertical-align:middle;border-top:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:none;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                        {web}/7</td>
                    <td width="81"
                        style="width:61pt;color:black;text-align:center;vertical-align:middle;border-top:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:none;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                        {jrn}/7</td>
                    <td width="81"
                        style="border-top:none;border-left:none;width:61pt;color:black;text-align:center;vertical-align:middle;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                        {goal}/7</td>
                    <td width="81"
                        style="border-top:none;border-left:none;width:61pt;color:black;text-align:center;vertical-align:middle;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                        {total}/28</td>
                </tr>

            </tbody>
        </table><br>
    </div>
    <img src="https://quickchart.io/chart?width=80&height=80&c=%7B%0A%20%20type%3A%20%27radialGauge%27%2C%0A%20%20data%3A%20%7B%0A%20%20%20%20datasets%3A%20%5B%7B%0A%20%20%20%20%20%20data%3A%20%5B{(total*100)//28}%5D%2C%0A%20%20%20%20%20%20backgroundColor%3A%20getGradientFillHelper(%27horizontal%27%2C%20%5B%27blue%27%2C%20%27red%27%5D)%2C%0A%20%20%20%20%7D%5D%0A%20%20%7D%2C%0A%20%20options%3A%20%7B%0A%20%20%20%20%2F%2F%20See%20https%3A%2F%2Fgithub.com%2Fpandameister%2Fchartjs-chart-radial-gauge%23options%0A%20%20%20%20domain%3A%20%5B0%2C%20100%5D%2C%0A%20%20%20%20trackColor%3A%20%27%23f0f8ff%27%2C%20%0A%20%20%20%20centerPercentage%3A%2080%2C%0A%20%20%20%20centerArea%3A%20%7B%0A%20%20%20%20%20%20text%3A%20(val)%20%3D%3E%20val%20%2B%20%27%25%27%2C%0A%20%20%20%20%7D%2C%0A%20%20%7D%0A%7D">
    <div>Cheers,</div>
    <div>Hugo</div>
</div>"""


def main():

    past_days = input("How many days old is the report (enter for none)\n")
    if not past_days:
        past_days = 0
    past_days = int(past_days)

    count_dict = get_all_counts(7, past_days)

    med = count_dict["med"]
    web = count_dict["web"]
    jrn = count_dict["jrn"]
    goal = count_dict["goal"]
    total = sum((med, web, jrn, goal))
    grade = grade_total(total)

    for recipient in RECIPIENTS:
        html = fill_html(recipient[1], grade, med, web, jrn, goal, total)
        draft = create_draft(html, "Accountability Report", recipient[0])
        if draft:
            print(f"Draft created for {recipient[1]}")


if __name__ == "__main__":
    main()
