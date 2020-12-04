package acc_types;

public class RecurringAccount extends Account 
{
private double recurringAmt;
private int noOFInstallments;
private static float interest_rate;
static
{
	interest_rate=7.5f;
}

public RecurringAccount() {
	super();
	// TODO Auto-generated constructor stub
}
public RecurringAccount(int accno, String name, double balance, double recurringAmt, int noOFInstallments) {
	super(accno, name, balance);
	this.recurringAmt = recurringAmt;
	this.noOFInstallments = noOFInstallments;
}
@Override
public String toString() {
	// TODO Auto-generated method stub
	return super.toString()+"\nRecurring Amount:"+recurringAmt+"\nNo of Installments:"+noOFInstallments;
}
@Override
public void withdraw(double amt) 
{
	System.out.println("\nInvalid operation!!!.....couldnt withdraw cash");
	
}
@Override
public void calBalance() 
{

double a=recurringAmt*noOFInstallments;
balance=a+((a*interest_rate)/100);
System.out.println("Balance:"+balance);
}


}
