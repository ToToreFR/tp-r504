import java.io.*;
import java.net.*;

public class ServeurTCP3
{
    public static void main( String[] args ) throws Exception
    {
        ServerSocket socketserver = new ServerSocket( 2016 );
        while(true)
        {
        System.out.println( "serveur en attente" );
        Socket socket = socketserver.accept();
        System.out.println( "Connection d'un client" );
        DataInputStream dIn = new DataInputStream(socket.getInputStream());
        String msg = dIn.readUTF();
        String rev = new StringBuilder(msg).reverse().toString();
        System.out.println( "Message: " + rev);
        DataOutputStream dOut = new DataOutputStream(socket.getOutputStream());
        dOut.writeUTF( rev );
        socket.close();
        }
    }
}
