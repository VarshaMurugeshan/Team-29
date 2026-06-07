
from diff_engine import compare
from ai_agent import analyze

changes = compare('schemas/schema_day1.json','schemas/schema_day2.json')
report = analyze(changes)

for item in report:
    print(item)
