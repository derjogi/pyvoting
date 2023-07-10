"""
author: Yichen Zhang
"""
import pandas as pd
from PluralityVoting import PluralityVoting
from ApprovalVoting import ApprovalVoting
from ScoreVoting import ScoreVoting
from STARVoting import STARVoting
from RankedChoiceVoting import RankedChoiceVoting

if __name__ == "__main__":
    
    candidates = ["Trump","Pence","Biden"]
    election = RankedChoiceVoting(candidates, try_handle_invalid=True, 
                                  reverse=False, allowed_rank=0)
    #print(election.ImportBallots("ballot.xlsx"))
    
    print(election.AddBallot(pd.Series({"Trump":1,
                                        "Pence":2,
                                        "Biden":3})))
    print(election.AddBallot(pd.Series({"Trump":2,
                                        "Pence":3,
                                        "Biden":1})))
    print(election.AddBallot(pd.Series({"Trump":3,
                                        "Pence":1,
                                        "Biden":2})))
    
    
    print(election.RunElection())
    print(election.ExportBallots("ballot.xlsx"))
    