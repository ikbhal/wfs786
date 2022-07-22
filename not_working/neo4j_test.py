# pip install neo4j
# https://neo4j.com/developer/python/
# download neo4j desktop
# download from https://neo4j.com/download-thanks-desktop/?edition=desktop&flavour=winstall64&release=1.4.15&offline=true
# license
"""
eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Ii4rQC4rIiwibWl4cGFuZWxJZCI6IjE4MjAwMDhiZjljNzYwLTAyNWIyZTYzODc1OWRmLTY3M2I1NzUzLTE0NDAwMC0xODIwMDA4YmY5ZDEwNzEiLCJtaXhwYW5lbFByb2plY3RJZCI6IjRiZmIyNDE0YWI5NzNjNzQxYjZmMDY3YmYwNmQ1NTc1Iiwib3JnIjoiLioiLCJwdWIiOiJuZW80ai5jb20iLCJyZWciOiIgIiwic3ViIjoibmVvNGotZGVza3RvcCIsImV4cCI6MTY4OTkxODc1MSwidmVyIjoiKiIsImlzcyI6Im5lbzRqLmNvbSIsIm5iZiI6MTY1ODM4Mjc1MSwiaWF0IjoxNjU4MzgyNzUxLCJqdGkiOiJRbTNYNGo3WV8ifQ.vlWYDoxLnKy9AHICrNu6f5qgp4WNril53uwAe4pz1COwflWATeBHcyfSGLT4pABHtgnmRldGVdhhJA9gqWbm1MS9Q-slkroXhhNfS7ho3hUaStSwX8v7Rn0HpVKUwmhWQijVwBd0W6_LPm8uIctOD_efcx9c6Vgyn5p5LJvnQnZYJoR7wW_tF-nlreLF4VoKNSWMHxFVLdu3lQdl65Ri7nUwN-AmOPXr4944i6I_7TJHPgqHSq-8zD6-ZlHR2huF6hMwtVghgwaNyGWfA_hgkMvGzHdI3rEMRdMSRbzsi15amBE6mDyp6m1Zvlow21F8PsdpM7WT1qf6tNs1JOhE8Q
"""
# uri localhost:7474
# username neo4j
# password neo4j
# or try neo4j sandbox https://neo4j.com/sandbox/
# url https://797ed509f55b8dd93dc27989aa0d9540.neo4jsandbox.com/browser/?token=pwfetch:797ed509f55b8dd93dc27989aa0d9540:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFUbENPRVV4UmtJNFJETkROakpETXpBME5EZzBRelV3UWpNek9UVTVNRFF4TlRKRk56STJOZyJ9.eyJlbWFpbCI6ImlxYmFsZm9yYWxsQGdtYWlsLmNvbSIsIm5hbWUiOiJzaGFpayBpa2JoYWwgQmFzaGEiLCJnaXZlbl9uYW1lIjoic2hhaWsgaWtiaGFsIiwiZmFtaWx5X25hbWUiOiJCYXNoYSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BSXRidm1tMUw4RzNwQ3Rkb1lPR2dLbTR4cVprTUZ6czlVeWFQNV9LcGNxTj1zOTYtYyIsImxvY2FsZSI6ImVuLUdCIiwibmlja25hbWUiOiJpcWJhbGZvcmFsbCIsImFwcF9tZXRhZGF0YSI6eyJzYW5kYm94djMiOnsiY3JlYXRlZEF0IjoxNTk1NjA5NDAzOTI1LCJhZ3JlZWRUb1Rlcm1zQXQiOjE1OTU2MDk0MDc0NjF9fSwic2FuZGJveHYzIjp7ImNyZWF0ZWRBdCI6MTU5NTYwOTQwMzkyNSwiYWdyZWVkVG9UZXJtc0F0IjoxNTk1NjA5NDA3NDYxfSwiZmlyZWJhc2VfZGF0YSI6eyJ1aWQiOiJnb29nbGUtb2F1dGgyfDEwODUzMTQxNjAzMTk3NzYwODAzOCJ9LCJzY29wZXMiOnsic2FuZGJveGVzIjpbInNib3gxIiwic2JveDIiLCJzYm94MyJdfSwiZW1haWxfdmVyaWZpZWQiOnRydWUsImNsaWVudElEIjoiRHhobWlGOFRDZXpuSTdYb2kwOFV5WVNjTEdabms0a2UiLCJ1cGRhdGVkX2F0IjoiMjAyMi0wNy0yMVQwNjowNzoxOS4xNzBaIiwidXNlcl9pZCI6Imdvb2dsZS1vYXV0aDJ8MTA4NTMxNDE2MDMxOTc3NjA4MDM4IiwiaWRlbnRpdGllcyI6W3sicHJvdmlkZXIiOiJnb29nbGUtb2F1dGgyIiwidXNlcl9pZCI6IjEwODUzMTQxNjAzMTk3NzYwODAzOCIsImNvbm5lY3Rpb24iOiJnb29nbGUtb2F1dGgyIiwiaXNTb2NpYWwiOnRydWV9XSwiY3JlYXRlZF9hdCI6IjIwMTktMDQtMzBUMDY6NTQ6MTguOTk3WiIsInVzZXJfbWV0YWRhdGEiOnt9LCJpc3MiOiJodHRwczovL2xvZ2luLm5lbzRqLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwODUzMTQxNjAzMTk3NzYwODAzOCIsImF1ZCI6IkR4aG1pRjhUQ2V6bkk3WG9pMDhVeVlTY0xHWm5rNGtlIiwiaWF0IjoxNjU4MzgzNjQxLCJleHAiOjE2NTg0NzAwNDEsIm5vbmNlIjoiWW10TFNEZEVjRXRtUW1ReVYyOXJOMHc0UmpRd2JEVnpWRFp2WTFCdVpVNHpWRXhNTWs0MU1VMXZUZz09In0.Jg4olWvAWKyJdGKhjKXV1kMrNK-J_OCQP3D7NS6KNNnuSAd5oblIcWC1G7od99MWSq8EkYkkbkJ_7g6CoO0xh9-xSJkh1CeO-IAK9ekR04x_V36yliq0TjqaugPGmBOruKQaLZx_EKPDMiuzxFxLn-zz-I_AfU7Xl2OZ-n5x6fPr2GA0JCG_tLBMe3wFu5nWPsCfHHo1n8ie_Cbr4S-4-iz95yyy09Ym_bPfdTSYjH7NEIweDl5s115A52rOVc9xWoydwKghgUtASY3t_vscUWhiWwkhPW4_qnv0vMX-scGsr07Ey-NP6x5qxMCgeuJmMHODlo97gOqYzqlZhPJeiw
# You are connected as user neo4j
#to bolt+s://797ed509f55b8dd93dc27989aa0d9540.neo4jsandbox.com:7687 -> not working

# triying turtorial https://singerlinks.com/2020/11/how-to-connect-to-neo4j-using-the-python-driver/
from neo4j import GraphDatabase

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]


if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "neo4j")
    # greeter = HelloWorldExample("bolt://127.0.0.1:7687", "neo4j", "neo4j")
    # uri = "bolt+s://797ed509f55b8dd93dc27989aa0d9540.neo4jsandbox.com:7687"
    """
    https://singerlinks.com/2020/11/how-to-connect-to-neo4j-using-the-python-driver/
    bolt+s	BoltDriver with encryption (accepts only certificates signed by a certificate authority), full certificate checks.
    """
    # uri = "neo4j://797ed509f55b8dd93dc27989aa0d9540.neo4jsandbox.com:7687"
    # user= "ikbhal"
    # password="password"
    # greeter = HelloWorldExample(uri, user, password)
    greeter.print_greeting("hello, world")
    greeter.close()
