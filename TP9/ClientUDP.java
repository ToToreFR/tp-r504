import java.io.*;
import java.net.*;

public class ClientUDP
{
    public static void main( String[] args ) throws Exception
    {
        InetAddress addr = InetAddress.getLocalHost ();
        System.out.println( "adresse=" +addr.getHostName() );

        String s="Hello World";
        byte [ ] data = s . getBytes ( );

        DatagramPacket packet = new DatagramPacket( data, data.length, addr, 1234 );
        DatagramSocket sock = new DatagramSocket();
        sock.send(packet);
        sock.close();
        
        DatagramPacket response = new DatagramPacket(new byte[1024], 1024);
        sock.receive(response);
        String  = new String(packet.getData() );
    }
}
