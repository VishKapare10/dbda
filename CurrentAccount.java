package acc_types;

public class CurrentAccount extends Account
{
private double overdraft_amt;

public CurrentAccount() 
{
	super();
	// TODO Auto-generated constructor stub
}



public CurrentAccount(int accno, String name, double balance, double overdraft_amt) {
	super(accno, name, balance);
	this.overdraft_amt = overdraft_amt;
}



@Override
public String toString() {
	// TODO Auto-generated method stub
	return super.toString()+"\nOverdraft_amount"+overdraft_amt;
}



@Override
public void withdraw(double amt)
{
	if(balance>=amt)
	{
		balance=balance-amt;
		System.out.println(amt+"successfully withdrawn");
		System.out.println("Balance"+balance);
		System.out.println("Overdraft amt:"+overdraft_amt);
	}
	else if(amt<(balance+overdraft_amt))
	{
		//balance=0;
		overdraft_amt=overdraft_amt-(amt-balance);
		balance=0;
		System.out.println(amt+"successfully withdrawn");
		System.out.println("Balance"+balance);
		System.out.println("Overdraft amt:"+overdraft_amt);
		
	}
	else if(amt>balance+overdraft_amt)
	{
		System.out.println("Insufficient Balance");
	}
}



@Override
public void calBalance() 
{
	int charges=0;
	if(overdraft_amt<=100000)
	{
		System.out.println("Final Balance:"+(balance-5000));
	}
	else if(overdraft_amt>100000 && overdraft_amt<500000) 
	{
		System.out.println("Final Balance:"+(balance-7000));
	}
	else if(overdraft_amt>100000 && overdraft_amt<500000)
	{
		System.out.println("Final Balance:"+(balance-10000));
		
	}
	
}








}
