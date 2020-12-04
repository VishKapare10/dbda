package acc_types;

public abstract class Account 
{
	private int accno;
	private String name;
	protected double balance;
	
	

	public Account() 
	{
		
	}



	public Account(int accno, String name, double balance) 
	{
		super();
		this.accno = accno;
		this.name = name;
		this.balance = balance;
	}



	@Override
	public String toString() 
	{
	
		return "\nAccount No:"+accno+"\nName:"+name+"\nBalance:"+balance;
	}

	public abstract void withdraw(double amt);

	public abstract void calBalance();

	
}
