using System;
using System.Diagnostics;
using System.IO;

public class Program
{
    public static void Main()
    {
        // Obtener la ruta del escritorio utilizando USERPROFILE
        string exePath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), "Desktop", "Leveling", "report.exe");
        
        // Argumento de texto que quieres pasar al .exe
        string argument = "¡Tu personaje ha muerto!";

        // Configuramos el proceso
        ProcessStartInfo startInfo = new ProcessStartInfo
        {
            FileName = exePath,
            Arguments = argument,  // Pasamos el argumento aquí
            UseShellExecute = false,  // No usar la shell del sistema
            RedirectStandardOutput = true,  // Si deseas capturar la salida del .exe
            RedirectStandardError = true,   // Si deseas capturar los errores del .exe
            CreateNoWindow = true  // No mostrar ventana de consola
        };

        // Ejecutamos el proceso
        using (Process process = Process.Start(startInfo))
        {
            // Capturamos la salida del .exe
            string output = process.StandardOutput.ReadToEnd();
            string error = process.StandardError.ReadToEnd();

            process.WaitForExit();  // Esperamos a que el proceso termine

            // Mostramos la salida en consola
            Console.WriteLine("Output: " + output);
            Console.WriteLine("Error: " + error);
        }
    }
}