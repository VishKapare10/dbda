package acc_types;

public class AccountDemo {

	public static void main(String[] args)
	{
		Account[] accounts= { new SavingsAccount(19870,"Abhay",5000),
								new CurrentAccount(19876,"Jafar",50000,100000.0),
								new RecurringAccount(19999,"Ashish",500,5000,5)};
		
		for(int i=0;i<accounts.length;i++)
		{
			System.out.println(accounts[i]);
			System.out.println("*******************");
		}
		/*Account a1=new SavingsAccount(19870,"Abhay",5000);
		a1.withdraw(5000);
		a1.withdraw(1000);
		
		Account a2=new CurrentAccount(19876,"Jafar",50000,100000.0);
		a2.withdraw(60000);
		a2.withdraw(200000);
		
		Account a3=new RecurringAccount(19999,"Ashish",500,5000,5);
		a3.withdraw(5000);
		
		Account a1=new SavingsAccount(19870,"Abhay",5000);
		a1.calBalance();
		
		
		Account a3=new RecurringAccount(19999,"Ashish",500,5000,5);
		a3.calBalance(); 
		
		Account a2=new CurrentAccount(19876,"Jafar",50000,100000.0);
		a2.withdraw(50000);
		a2.withdraw(70000);
		a2.withdraw(40000);
		
		Account a3=new RecurringAccount(19999,"Ashish",500,5000,5);
		a3.calBalance(); */
		
	}

}
