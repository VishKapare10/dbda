package acc_types;



public class SavingsAccount extends Account 
{
	private static float interest_rate;
	static
	{
		interest_rate=4.5f;
	}
	public SavingsAccount() {
		super();
		
	}
	
	public SavingsAccount(int accno, String name, double balance) 
	{
		super(accno, name, balance);
		
	}
	
	@Override
	public String toString() 
	{
			return super.toString();
	}



	@Override
	public void withdraw(double amt) 
	{
		if(amt>balance-1000)
		{
			System.out.println("Insufficient balance!!!");
		}
		else
		{	balance=balance-amt;
			System.out.println(+amt+"\nAmount withdrawn successfully");
			System.out.println("Updated balance:"+balance);
			
		}
	}

	@Override
	public void calBalance()
	{
	balance=balance+((balance*7.5)/100);
	System.out.println("Updated Balance:"+balance);
		
	}

	
	
	
}
