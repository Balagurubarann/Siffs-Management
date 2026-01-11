# Account Creation

from src.model import SeparateSavingAccount, CreditAccount, ContinuousSavingAccount
from src.extension import db

def account_creation_async(holder_id, acc_no, created_by):

    separateSavingAccount = SeparateSavingAccount(
        holder_id=holder_id,
        acc_no=acc_no,
        created_by=created_by
    )

    continuousSavingAccount = ContinuousSavingAccount(
        holder_id=holder_id,
        acc_no=acc_no,
        created_by=created_by
    )

    creditAccount = CreditAccount(
        holder_id=holder_id,
        acc_no=acc_no,
        created_by=created_by
    )

    db.session.add(creditAccount)
    db.session.add(separateSavingAccount)
    db.session.add(continuousSavingAccount)

    db.commit()
