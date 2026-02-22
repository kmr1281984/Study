CCNP 350-401 (ENCOR) Quiz System

Files Included

-   ccnp_350_401_150q.csv -> 150-question question bank
-   cisco_quiz_runner.py -> Quiz engine (domain filtering supported)

CSV Structure

Required columns:

id,domain,type,question,A,B,C,D,answer

Optional columns:

explanation,tags

Field Details: - domain: Architecture, Virtualization, Infrastructure,
Network Assurance, Security, Automation - type: single | multi - answer:
single -> B multi -> A;C

Example Row: 1,Infrastructure,single,“Which protocol uses Hello
packets?”, BGP,OSPF,SNMP,FTP,B,“OSPF uses Hello packets.”,“ospf;routing”

Basic Usage

List available domains: python cisco_quiz_runner.py –csv
ccnp_350_401_150q.csv –list-domains

Quiz a single domain: python cisco_quiz_runner.py –csv
ccnp_350_401_150q.csv –domains “Infrastructure”

Quiz multiple domains: python cisco_quiz_runner.py –csv
ccnp_350_401_150q.csv –domains “Infrastructure,Security”

Shuffle and limit questions: python cisco_quiz_runner.py –csv
ccnp_350_401_150q.csv –shuffle –limit 25

Weighted domain selection: python cisco_quiz_runner.py –csv
ccnp_350_401_150q.csv –limit 30 –weighted

Timed mode (Unix/macOS best support): python cisco_quiz_runner.py –csv
ccnp_350_401_150q.csv –time-per-q 60

Review missed questions: python cisco_quiz_runner.py –csv
ccnp_350_401_150q.csv –review-missed

Save results: python cisco_quiz_runner.py –csv ccnp_350_401_150q.csv
–save results.jsonl

Study Recommendations

-   Use –domains to focus on weak blueprint areas.
-   Use –limit 20 for quick daily drills.
-   Use –review-missed to reinforce weak concepts.
-   Track progress over time with –save.

Good luck on your CCNP 350-401 (ENCOR) exam!
