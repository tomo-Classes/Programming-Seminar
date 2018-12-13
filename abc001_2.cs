using System;
class abc001_2 {
	static void Main(string[] args) {
		int input = int.Parse(Console.ReadLine());
		double m = 1.0 * input / 1000;
		double vv;
		if(m < 0.1) {
			vv = 0;
		} else if(m <= 5) {
			vv = m * 10;
		} else if(m <= 30) {
			vv = m + 50;
		} else if(m <= 70) {
			vv = (m - 30) / 5 + 80;
		} else {
			vv = 89;
		}
		string ret = "0" + vv;
		ret = ret.Substring(ret.Length - 2, 2);
		Console.WriteLine(ret);
	}
}
