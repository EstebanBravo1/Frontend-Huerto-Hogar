#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para crear ramas Git, comprimir frontend y backend
"""

import os
import shutil
import subprocess
from pathlib import Path

PROJECT_ROOT = r"c:\Users\esteb\OneDrive\Desktop\Proyecto Final\Proyecto Final"
os.chdir(PROJECT_ROOT)

def run_command(cmd):
    """Ejecutar comando de shell"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def crear_rama_frontend():
    """Crear rama frontend y agregar archivos"""
    print("Creando rama frontend...")
    
    # Crear rama
    ret, out, err = run_command("git branch frontend")
    if ret == 0:
        print("Rama frontend creada")
    else:
        print("Error crear rama frontend: " + err)
    
    # Cambiar a rama frontend
    ret, out, err = run_command("git checkout frontend")
    if ret == 0:
        print("Cambiado a rama frontend")
    else:
        print("Error cambiar rama: " + err)
    
    # Agregar archivos del frontend
    print("Agregando archivos del frontend...")
    
    # Iniciar commit
    run_command("git add DSY1104-Bravo-Sarria/")
    run_command("git add Documentos_Generados/Manual_Usuario_Huerto_Hogar.docx")
    
    ret, out, err = run_command('git commit -m "Frontend: Archivos del proyecto React"')
    if ret == 0:
        print("Commit frontend realizado")
    else:
        print("Nota: " + err)

def crear_rama_backend():
    """Crear rama backend y agregar archivos"""
    print("Creando rama backend...")
    
    # Cambiar a main primero
    run_command("git checkout -b main 2>nul || git checkout main")
    
    # Crear rama
    ret, out, err = run_command("git branch backend")
    if ret == 0:
        print("Rama backend creada")
    else:
        print("Error crear rama backend: " + err)
    
    # Cambiar a rama backend
    ret, out, err = run_command("git checkout backend")
    if ret == 0:
        print("Cambiado a rama backend")
    else:
        print("Error cambiar rama: " + err)
    
    # Agregar archivos del backend
    print("Agregando archivos del backend...")
    
    run_command("git add backend/")
    run_command("git add sales/")
    run_command("git add users-service/")
    run_command("git add Documentos_Generados/Documentacion_APIs_Huerto_Hogar.docx")
    run_command("git add Documentos_Generados/Integracion_APIs_Huerto_Hogar.docx")
    
    ret, out, err = run_command('git commit -m "Backend: Archivos de microservicios Spring Boot"')
    if ret == 0:
        print("Commit backend realizado")
    else:
        print("Nota: " + err)

def comprimir_frontend():
    """Comprimir frontend en ZIP"""
    print("Comprimiendo frontend...")
    
    frontend_path = os.path.join(PROJECT_ROOT, "DSY1104-Bravo-Sarria")
    output_path = os.path.join(PROJECT_ROOT, "frontend.zip")
    
    if os.path.exists(output_path):
        os.remove(output_path)
    
    shutil.make_archive(
        os.path.join(PROJECT_ROOT, "frontend"),
        "zip",
        PROJECT_ROOT,
        "DSY1104-Bravo-Sarria"
    )
    
    if os.path.exists(output_path):
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print("Frontend comprimido: frontend.zip ({:.2f} MB)".format(size_mb))
        return output_path
    else:
        print("Error comprimiendo frontend")
        return None

def comprimir_backend():
    """Comprimir backend en ZIP"""
    print("Comprimiendo backend...")
    
    backend_dirs = ["backend", "sales", "users-service"]
    output_path = os.path.join(PROJECT_ROOT, "backend.zip")
    
    if os.path.exists(output_path):
        os.remove(output_path)
    
    # Crear archivo ZIP temporal
    with shutil.ZipFile(output_path, "w", shutil.ZIP_DEFLATED) as zipf:
        for dir_name in backend_dirs:
            dir_path = os.path.join(PROJECT_ROOT, dir_name)
            if os.path.exists(dir_path):
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, PROJECT_ROOT)
                        zipf.write(file_path, arcname)
    
    if os.path.exists(output_path):
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print("Backend comprimido: backend.zip ({:.2f} MB)".format(size_mb))
        return output_path
    else:
        print("Error comprimiendo backend")
        return None

def ir_a_main_y_comprimir():
    """Cambiar a main y colocar archivos comprimidos"""
    print("Cambiando a rama main...")
    
    # Crear main si no existe
    run_command("git checkout -b main 2>nul || git checkout main")
    
    print("Preparando archivos comprimidos en main...")
    
    # Los archivos ya deben estar en el directorio raiz
    # Solo necesitamos agregarlos a git
    run_command("git add frontend.zip backend.zip")
    
    ret, out, err = run_command('git commit -m "Archivos comprimidos: frontend.zip y backend.zip"')
    if ret == 0:
        print("Commit main realizado con archivos comprimidos")
    else:
        print("Nota: " + err)

def main():
    print("=" * 60)
    print("INICIANDO GESTION DE RAMAS Y COMPRESION")
    print("=" * 60)
    
    try:
        # Primero hacer commit inicial en main
        print("Realizando commit inicial...")
        run_command("git add -A")
        run_command('git commit -m "Commit inicial del proyecto"')
        
        # Crear ramas
        crear_rama_frontend()
        crear_rama_backend()
        
        # Comprimir
        frontend_zip = comprimir_frontend()
        backend_zip = comprimir_backend()
        
        # Ir a main y agregar archivos comprimidos
        ir_a_main_y_comprimir()
        
        print()
        print("=" * 60)
        print("GESTION DE RAMAS Y COMPRESION COMPLETADA")
        print("=" * 60)
        print()
        print("Ramas creadas:")
        print("  - frontend")
        print("  - backend")
        print("  - main (con archivos comprimidos)")
        print()
        
        # Listar ramas
        ret, out, err = run_command("git branch -a")
        print("Ramas disponibles:")
        print(out)
        
    except Exception as e:
        print("ERROR: " + str(e))
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
