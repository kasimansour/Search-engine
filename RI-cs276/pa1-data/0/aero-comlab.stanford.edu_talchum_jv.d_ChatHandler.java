import java io import java net import java util public class chathandler implements runnable protected socket socket public chathandler socket socket this socket socket protected datainputstream datain protected dataoutputstream dataout protected thread listener public synchronized void start if listener null try datain new datainputstream new bufferedinputstream socket getinputstream dataout new dataoutputstream new bufferedoutputstream socket getoutputstream listener new thread this listener start catch ioexception ignore public synchronized void stop if listener null try if listener thread currentthread listener interrupt listener null dataout close catch ioexception ignored protected static vector handlers new vector public void run try handlers addelement this string outputline inputline outputline your id dataout writeutf outputline dataout flush inputline datain readutf dataout writeutf welcome inputline+ have a nice time dataout flush listener setname inputline while thread interrupted inputline datain readutf string name listener getname string message name inputline broadcast message catch eofexception ignored catch ioexception ex if listener thread currentthread ex printstacktrace finally handlers removeelement this stop protected void broadcast string message synchronized handlers enumeration enum handlers elements while enum hasmoreelements chathandler handler chathandler enum nextelement try handler dataout writeutf message handler dataout flush catch ioexception ex handler stop