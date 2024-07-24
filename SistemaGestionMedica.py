import os
from datetime import datetime

class Pacientes:
    def __init__(self,paciente,cedula,edad,genero,peso,caso,celular,direccion):
        self.paciente  = paciente
        self.cedula = cedula
        self.edad = edad
        self.genero = genero
        self.peso = peso
        self.caso = caso
        self.celular = celular
        self.direccion = direccion

    def AgregarPaciente(self, listaPacientes):
        print("LLegamos hasta aqui para agregar pacientes")
        print("Agregar los siguientes datos, por favor :)")
        print("-------------------------------------------------------------")
        while True:
            try:
                self.cedula = str(input("Ingrese numero de cedula, por favor: ").strip())
                if not self.cedula:
                    raise ValueError("Ingrese su cedula, por favor :)")
                cedulaExistente = any(p.cedula == self.cedula for p in listaPacientes)
                if cedulaExistente:
                    raise ValueError("La cedula ya fue registrada con anterioridad")
                
                break
            except ValueError as e:
                print(e)
                print("Intente de nuevo, y no vuelva a fallar")    

        #Nombre del paciente
        while True:
            try:
                self.paciente = str(input("Ingrese su nombre completo :").strip().upper())
                if not self.paciente:
                    raise ValueError("Ingrese su nombre, :)")
                break
            except ValueError as e:
                print(e)
                print("Intente de nuevo\n")
        #Cedula del paciente
        
        #edad del paciente
        while True:
            try:
                self.edad = int(input("Ingrese edad, por favor: ").strip())
                if not self.edad:
                    raise ValueError("Ingrese su edad, por favor :)")
                break
            except ValueError as e:
                print(e)
                print("Intente de nuevo, y no vuelva a fallar")
        #Genero de la persona
        while True:
            try:
                self.genero = str(input("Ingrese su genero (M/F) :").strip().upper())
                if self.genero not in ['m','f','F','M']:
                    raise ValueError("Ingrese su genero (M/F) :)")
                break
            except ValueError as e:
                print(e)
                print("Intente de nuevo\n")
        #Peso del paciente
        while True:
            try:
                self.peso = float(input("Ingrese su peso en libras, por favor: ").strip())
                if not self.peso:
                    raise ValueError("Ingrese su peso en libras, por favor :)")
                break
            except ValueError as e:
                print(e)
                print("Intente de nuevo, y no vuelva a fallar")
        #Caso que se va a atender - en este es una cadena de texto
        while True:
            try:
                self.caso = str(input("Ingrese el caso clinico :").strip().upper())
                if not self.caso:
                    raise ValueError("Ingrese el caso clinico, :)")
                break
            except ValueError as e:
                print(e)
                print("Intente de nuevo\n")
        #Celular o numero de contacto del paciente
        while True:
            try:
                self.celular = int(input("Ingrese numero de celular, por favor: ").strip())
                if not self.celular:
                    raise ValueError("Ingrese su celular, por favor :)")
                break
            except ValueError as e:
                print(e)
                print("Intente de nuevo, y no vuelva a fallar")
        #Direccion del paciente - por si se requiere
        while True:
            try:
                self.direccion = str(input("Ingrese su direccion completa :").strip().upper())
                if not self.direccion:
                    raise ValueError("Ingrese su direccion completa, :)")
                break
            except ValueError as e:
                print(e)
                print("Intente de nuevo\n")
        print("-------------------------------------------------------------")
        return self
    
    def QuitarPaciente(self, listaPacientes, cedula):
        encontrado = False
        for p in listaPacientes:
            if p.cedula == cedula:
                listaPacientes.remove(p)
                print(f"La Persona con cedula {cedula} ha sido removida")
                encontrado = True
                break
        if not encontrado:
            print("El paciente no fue encontrado")

    def ModificarPaciente(self, listaPacientes, cedula):
        encontrado = False
        for p in listaPacientes:
            if p.cedula == cedula:
                print("Modificar paciente\n")
                print(f"Información actual del paciente con cédula {cedula}:")
                p.InfoPaciente(listaPacientes,cedula)  
                print("------------------------------------------")
                # Permitir al usuario modificar los atributos seleccionados
                while True:
                    print("Seleccione el atributo que desea modificar:")
                    print("1. Edad")
                    print("2. Peso")
                    print("3. Caso")
                    print("4. Celular")
                    print("0. Terminar la modificación")
                    opcion = input("Ingrese el número de la opción: ").strip()

                    if opcion == "0":
                        break

                    elif opcion == "1":
                        while True:
                            try:
                                nueva_edad = int(input("Ingrese la nueva edad: ").strip())
                                p.edad = nueva_edad
                                break
                            except ValueError:
                                print("Por favor, ingrese un valor numérico para la edad.")

                    elif opcion == "2":
                        while True:
                            try:
                                nuevo_peso = float(input("Ingrese el nuevo peso en libras: ").strip())
                                p.peso = nuevo_peso
                                break
                            except ValueError:
                                print("Por favor, ingrese un valor numérico para el peso.")

                    elif opcion == "3":
                        nuevo_caso = input("Ingrese el nuevo caso clínico: ").strip().upper()
                        p.caso = nuevo_caso

                    elif opcion == "4":
                        while True:
                            try:
                                nuevo_celular = int(input("Ingrese el nuevo número de celular: ").strip())
                                p.celular = nuevo_celular
                                break
                            except ValueError:
                                print("Por favor, ingrese un valor numérico para el celular.")

                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")

                print(f"Paciente con cédula {cedula} modificado correctamente.")
                print("------------------------------------------")
                encontrado = True
                break
        
        if not encontrado:
            print(f"No se encontró al paciente con cédula {cedula}.")
    #Con esta imprimimos toda la lista de pacientes registrados
    def ImprimirLista(listaPacientes):
        print("--------------------------------------")
        print("Lista de pacientes :")
        for p in listaPacientes:
            print("Paciente :")
            print(f"Nombre: {p.paciente}\tCedula: {p.cedula}\tGenero: {p.genero}\tEdad: {p.edad}\tCaso: {p.caso}")
        print("--------------------------------------")

    #Con esto imprimimos los datos del paciente, nos puede dar la cedula o el nombre
    #Modo de prueba
    #aquí se modifico para que solo mande datos, la validacion esta abajo en la
    #funcion de las opciones de paciente
    def InfoPaciente(self,listaPacientes,info):
        encontrado = False
        for p in listaPacientes:
            if p.cedula == info:
                encontrado = True
                print("------------------------")
                print(f"Nombre :{p.paciente}")
                print(f"Cedula :{p.cedula}")
                print(f"Edad :{p.edad}")
                print(f"Celular :(+593){p.celular}")
                print(f"Genero :{p.genero}")
                print(f"Direccion :{p.direccion}")
                print(f"Caso :{p.caso}")
                print(f"Peso :{p.peso}")
                print("--------------------------\n")   
            if not encontrado:
                print("Paciente no encontrado")    
            

class Citas:
    def __init__(self,paciente,cedula,fecha,hora,doctor,cedulaDoctor,especialidad):
        self.paciente = paciente
        self.cedula = cedula
        self.fecha = fecha
        self.hora = hora
        self.doctor = doctor
        self.cedulaDoctor = cedulaDoctor
        self.especialidad = especialidad

    def Agendar(self, listaCitas, listaPacientes, listaMedicos):
        while True:
            try:
                # Solicitamos los datos del paciente
                cedula = input("Ingrese la cédula del paciente: ").strip()
                paciente = next((p for p in listaPacientes if p.cedula == cedula), None)
                if not paciente:
                    raise ValueError("Paciente no encontrado.")
                
                # Mostrar la lista de los médicos disponibles
                Medicos.MedicosDisponibles(listaMedicos)
                print("-------------------------------------------------------------")
                # Pedimos los datos del doctor a registrar en la cita
                cedulaDoctor = input("Ingrese la cédula del médico: ").strip()
                doctor = next((p for p in listaMedicos if p.cedula == cedulaDoctor), None)
                if not doctor:
                    raise ValueError("Médico no encontrado.")
                
                # Solicitamos fecha y hora
                fecha = input("Ingrese la fecha de la cita (DD/MM/AAAA): ").strip()
                hora = input("Ingrese la hora de la cita (HH:MM): ").strip()
                print("-------------------------------------------------------------")

                # Convertir hora a minutos para comparación
                hora_minutes = int(hora.split(":")[0]) * 60 + int(hora.split(":")[1])

                # Verificar si ya existe una cita para el mismo médico en el mismo horario o dentro de una hora de diferencia
                for c in listaCitas:
                    if c.doctor == doctor.doctor and c.fecha == fecha:
                        cita_hora_minutes = int(c.hora.split(":")[0]) * 60 + int(c.hora.split(":")[1])
                        if abs(hora_minutes - cita_hora_minutes) < 60:
                            raise ValueError("Ya existe una cita para este médico en el mismo horario o dentro de una hora de diferencia.")

                # Crear una nueva cita
                cita = Citas(paciente.paciente, paciente.cedula, fecha, hora, doctor.doctor,doctor.cedula, doctor.especializacion)
                listaCitas.append(cita)
                print(f"Cita agendada para {paciente.paciente} con el Dr. {doctor.doctor} ({doctor.especializacion}) el {fecha} a las {hora}.")
                break

            except ValueError as e:
                print(e)
                print("Intente de nuevo.")

        return cita

    def ConsultarHorarioMedico(self, listaCitas, cedulaDoctor):
        print(f"Consultando horarios para el médico con cédula {cedulaDoctor}")
        print("-------------------------------------------------------------")
        citasDelMedico = [c for c in listaCitas if c.cedulaDoctor == cedulaDoctor]
        if citasDelMedico:
            citasDelMedico.sort(key=lambda c: datetime.strptime(c.fecha, "%d/%m/%Y"))
            for c in citasDelMedico:
                print(f"Paciente: {c.paciente} - Fecha: {c.fecha} - Hora: {c.hora}")
        else:
            print(f"No hay citas agendadas para el médico con cédula {cedulaDoctor}.")
        print("-------------------------------------------------------------")


    def ConsultarFechaPaciente(self, listaCitas, cedulaPaciente):
        print(f"Consultando fechas para el paciente con cédula {cedulaPaciente}")
        print("-------------------------------------------------------------")
        citasDelPaciente = [c for c in listaCitas if c.cedula == cedulaPaciente]
        if citasDelPaciente:
            for c in citasDelPaciente:
                print(f"Fecha: {c.fecha} - Hora: {c.hora} - Doctor: {c.doctor} - Especialidad: {c.especialidad}")
        else:
            print(f"No hay citas agendadas para el paciente con cédula {cedulaPaciente}.")
        print("-------------------------------------------------------------")

    def CambiarCita(self, listaCitas, cedulaPaciente, nuevaFecha, nuevaHora):
        print(f"Cambiando cita para el paciente con cédula {cedulaPaciente}")
        citaEncontrada = False
        for c in listaCitas:
            if c.cedula == cedulaPaciente:
                print(f"Cita actual: Fecha: {c.fecha} - Hora: {c.hora} - Doctor: {c.doctor} - Especialidad: {c.especialidad}")
                c.fecha = nuevaFecha
                c.hora = nuevaHora
                print(f"Nueva cita: Fecha: {c.fecha} - Hora: {c.hora}")
                citaEncontrada = True
                break
        if not citaEncontrada:
            print(f"No se encontró cita para el paciente con cédula {cedulaPaciente}")

    def CancelarCita(self, listaCitas, cedulaPaciente):
        print(f"Cancelando cita para el paciente con cédula {cedulaPaciente}")
        citaEncontrada = False
        for c in listaCitas:
            if c.cedula == cedulaPaciente:
                listaCitas.remove(c)
                print(f"La cita para el paciente con cédula {cedulaPaciente} ha sido cancelada.")
                citaEncontrada = True
                break
        if not citaEncontrada:
            print(f"No se encontró cita para el paciente con cédula {cedulaPaciente}")

    @staticmethod
    def ImprimirLista(listaCitas):
        print("Listado de citas:")
        for c in listaCitas:
            print(f"Paciente: {c.paciente}\tCedula: {c.cedula}\tFecha: {c.fecha}\tHora: {c.hora}\tDoctor: {c.doctor}\tEspecialidad: {c.especialidad}")


class Medicos:
    def __init__(self,doctor,contacto,cedula,especializacion, horarios = None):
        self.doctor = doctor
        self.cedula = cedula
        self.contacto = contacto
        self.especializacion = especializacion
        if horarios is None:
            self.horarios = {
                "Lunes":[],
                "Martes":[],
                "Miercoles":[],
                "Jueves":[],
                "Viernes":[],
                "Sabado":[],
                "Domingo":[]
            }
        else:
            self.horarios = horarios

    def AgregarMedico(self,listaMedicos):
        print("-------------------------------------------------------------")
        while True:
            try:
                self.cedula = str(input("Ingrese numero de cedula, por favor: ").strip())
                if not self.cedula:
                    raise ValueError("Ingrese su numero de cedula: ")
                cedulaExistente = any(p.cedula == self.cedula for p in listaMedicos)
                if cedulaExistente:
                    raise ValueError("La cedula ya fue registrada con anterioridad")
                break
            except ValueError as e:
                print(e)
                print("Intente de nuevo")

        while True:
            try:
                self.doctor = str(input("Ingrese el nombre del doctor: ").strip().upper())
                if not self.doctor:
                    raise ValueError("Ingrese el nombre del medico: ")
                break
            except ValueError as e:
                print(e)
                print("Intente de nuevo\n")

        while True:
            try:
                self.contacto = int(input("Ingrese su numero de contacto, por favor: "))
                if not self.contacto:
                    raise ValueError("Ingrese informacion, por favor : ")
                break
            except ValueError as e:
                print(e)
                print("Intente de nuevo")

        while True:
            try:
                self.especializacion = str(input("Ingrese su especializacion :").strip().upper())
                if not self.especializacion:
                    raise ValueError("Ingrese la informacion, por favor :")
                break
            except ValueError as e:
                print(e)
                print("Intente de nuevo")
        print("-------------------------------------------------------------")
        return self

    def HorarioMedico(self):
        print(f"Horarios disponibles para el/la Dr.{self.doctor}")
        for dia, horarios in self.horarios.items():
            print(f"{dia}:")
            if horarios:
                for horario in horarios:
                    print(f" - {horario}")
                else:
                    print(f" - No hay horarios disponibles")

    def InfoMedico(self,listaMedicos,info):
        encontrado = False
        for p in listaMedicos:
            if p.cedula == info:
                encontrado = True
                print("------------------------")
                print(f"Nombre :{p.doctor}")
                print(f"Cedula :{p.cedula}")
                print(f"Celular :(+593){p.contacto}")
                print(f"Especializacion :{p.especializacion}")
                print("--------------------------\n")   
            if not encontrado:
                print("Paciente no encontrado")    

    def MedicosDisponibles(listaMedicos):
        print("---------------------------")
        print("Lista de Medicos disponibles:")
        for d in listaMedicos:
            print("Medico:")
            print(f"Doctor: {d.doctor}\tCedula: {d.cedula}\tContacto: (+593){d.contacto}\tEspecializacion: {d.especializacion}")
        print("---------------------------")

    def QuitarMedico(self,listaMedicos,cedula):
        encontrar = False
        for p in listaMedicos:
            if p.cedula == cedula:
                listaMedicos.remove(p)
                print(f"El medico con cedula {cedula} ha sido removido")
                encontrar = True
                break
            if not encontrar:
                print("El paciente no fue encontrado")

def main_menu(listaPacientes,listaCitas,listaMedicos):
    
    print("Buenos dias a 'nombre de la aplicacion', en que podemos ayudarle?\n")
    while True:
        print("----------------Menu Principal---------------------")
        print("|1. Pacientes.",
              "\n|2. Citas.",
              "\n|3. Medicos.",
              "\n|0. Salir")
        print("-------------------------------------------------")
        try:
            opcion = int(input("Ingrese el numero de la operacion que desea realiza:").strip())
            if opcion not in [0,1,2,3]:
                raise ValueError("Ingrese un valor de las opciones por favor :)")

        except ValueError as e:
            print(e)
            print("Intente de nuevo, por favor")
            continue

        if(opcion == 0):
            print("Gracias por ingresar y usar nuestra aplicacion ;)")
            break

        if ( opcion == 1):
            limpiar()
            PacienteMenu(listaPacientes)
            
                
        if (opcion == 2):
            limpiar()
            CitasMenu(listaCitas,listaPacientes,listaMedicos)
            

        if(opcion == 3):
            limpiar()
            MedicosMenu(listaMedicos,listaCitas)
            

def PacienteMenu(listaPacientes):
    
    while True:
        print("----------Menu pacientes-------------------\n")
        print("|1. Agregar paciente.",
              "\n|2. Quitar paciente.",
              "\n|3. Modificar informacion de paciente.",
              "\n|4. Informacion del paciente")
        print("|5. Lista de pacientes.",
              "\n|0. Salir.")
        print("-------------------------------------------")
        try:
                opcion = int(input("Ingrese el numero de la operacion que desea realiza:").strip())
                
                if opcion not in [0,1,2,3,4,5]:
                    raise ValueError("Ingrese un valor de las opciones por favor :)")
                
        except ValueError as e:
                print(e)
                print("Intente de nuevo, por favor")
                continue

        if(opcion == 1):
            limpiar()
            print("Agregar paciente\n")
            paci = Pacientes("","",0,"",0,"",0,"")
            #revisar si el paciente ya fue agregado previamente, usar T o F para ver si se procede o no
            paci.AgregarPaciente(listaPacientes)
            listaPacientes.append(paci)
            print("Paciente agregado :)\n")
        if(opcion == 2):
            limpiar()
            print("---------------------------------------")
            print("Quitar paciente\n")
            info = input("Ingrese la cedula del paciente :").strip()
            paci = Pacientes("","",0,"",0,"",0,"")
            paci.QuitarPaciente(listaPacientes, info)
        
        if(opcion == 3):
            limpiar()
            print("---------------------------------------")
            print("Informacion del paciente")
            info = input("Ingrese la cedula del paciente :").strip()
            paci.ModificarPaciente(listaPacientes,info)

        if(opcion == 4):
            limpiar()
            print("---------------------------------------")
            print("Informacion del paciente")
            info = input("Ingrese la cedula del paciente :").strip()
            paci.InfoPaciente(listaPacientes,info)
        
        #se puso el recorrido de la lista aquí ya que no funcionaba en la fun infoPaciente
        #aquí con esto vamos a ver si nos da la info
        if(opcion == 5):
             limpiar()
             Pacientes.ImprimirLista(listaPacientes)
   
        if(opcion == 0):
            limpiar()
            print("Salir de aquí\n")
            break

def CitasMenu(listaCitas,listaPacientes,listaMedicos):
    while True:
        print("------------Menu Citas---------------------\n")
        print("|1. Agendar.",
              "\n|2. Consultar Horarios del medico.",
              "\n|3. Consultar Fecha del paciente.",
              "\n|4. Modificar fecha de la cita.",
              "\n|5. Cancelar la cita.",
              "\n|0. Salir")
        print("-------------------------------------------")
            
        try:
            opcion = int(input("Ingrese el numero de la operacion que desea realiza:").strip())
            if opcion not in [0,1,2,3,4,5]:
                raise ValueError("Ingrese un valor de las opciones por favor :)")
        except ValueError as e:
            print(e)
            print("Intente de nuevo, por favor")
            continue

        #se modifico agregando el append para que registre la cita
        if(opcion == 1):
            limpiar()
            print("Agendar\n")
            cita = Citas("","","","","","","")
            cita.Agendar(listaCitas,listaPacientes,listaMedicos)
            listaCitas.append(cita)

        
        if(opcion == 2):
            limpiar()
            print("Consultar Horarios del medico\n")
            cedulaDoctor = input("Ingrese la cedula del medico: ").strip()
            cita = Citas("","","","","","","")
            cita.ConsultarHorarioMedico(listaCitas, cedulaDoctor)

        if(opcion == 3):
            limpiar()
            print("Consultar fecha del paciente\n")
            cedulaPaciente = input("Ingrese la cedula del paciente: ").strip()
            cita = Citas("","","","","","","")
            cita.ConsultarFechaPaciente(listaCitas, cedulaPaciente)

        if(opcion == 4):
            limpiar()
            print("Modificar fecha de la cita\n")
            cedulaPaciente = input("Ingrese la cedula del paciente: ").strip()
            nuevaFecha = input("Ingrese la nueva fecha (DD/MM/AAAA): ").strip()
            nuevaHora = input("Ingrese la nueva hora (HH:MM): ").strip()
            cita = Citas("","","","","","","")
            cita.CambiarCita(listaCitas, cedulaPaciente, nuevaFecha, nuevaHora)
        
        if(opcion == 5):
            limpiar()
            print("Cancelar la cita\n")
            cedulaPaciente = input("Ingrese la cedula del paciente: ").strip()
            cita = Citas("","","","","","","")
            cita.CancelarCita(listaCitas, cedulaPaciente)

        if(opcion == 0):
            limpiar()
            break

def MedicosMenu(ListaMedicos, listaCitas):
    #Tener medicos ya agregados par agilidad de prueba - aquì se los agrego
    

    while True:
        print("-------------------Menu Medico---------------------\n")
        print("|1. Agregar Medico al sistem.",
              "\n|2. Horario del medico.",
              "\n|3. Informacion del medico.",
              "\n|4. Medicos disponibles.",
              "\n|5. Quitar medico",
              "\n|0. Salir.")
        print("-------------------------------------------------")
        try:
            opcion = int(input("Ingrese el numero de la operacion que desea realiza:").strip())
            if opcion not in [0,1,2,3,4,5]:
                raise ValueError("Ingrese un valor de las opciones por favor :)")
        
        except ValueError as e:
            print(e)
            print("Intente de nuevo, por favor")
            continue

        if(opcion == 1):
            limpiar()
            print("Agregar Medico al sistem.\n")
            medi = Medicos("",0,"","",{})
            #revisar si el paciente ya fue agregado previamente, usar T o F para ver si se procede o no
            medi.AgregarMedico(ListaMedicos)
            ListaMedicos.append(medi)
            print("Nuevo medico agregado :)\n")

        if(opcion == 2):
            limpiar()
            #actualizacion del consultar horario del medico
            print("Horarios del medico\n")
            cedulaDoctor = input("Ingrese la cedula del medico: ").strip()
            cita = Citas("","","","","","","")
            cita.ConsultarHorarioMedico(listaCitas, cedulaDoctor)
        
        if(opcion == 3):
            limpiar()
            print("---------------------------------------")
            print("Informacion del medico")
            info = input("Ingrese la cedula del paciente :").strip()
            medi.InfoMedico(ListaMedicos,info)

        if(opcion == 4):
            limpiar()
            print("Medicos disponibles\n")
            Medicos.MedicosDisponibles(ListaMedicos)
  
        if(opcion == 5):
            limpiar()
            print("---------------------------------------")
            print("Quitar medico\n")
            info = input("Ingrese la cedula del Medico :").strip()
            medi = Medicos("",0,"","",{})
            medi.QuitarMedic(ListaMedicos, info)
                     

        if(opcion == 0):
            limpiar()
            break

def menuDoctor(listaPacientes,listaCitas,ListaMedicos):
    medi = Medicos("",0,"","",{})
    cita = Citas("","","","","","","")
    paci = Pacientes("","",0,"",0,"",0,"")
    while True:
        print("------------------Menu Doctor-------------------------------\n")
        print("|1. Horario del medico.",
              "\n|2. cita del paciente.",
              "\n|3. Informacion del medico.",
              "\n|4. Medicos disponibles.",
              "\n|5. Lista de pacientes",
              "\n|0. Salir.")
        print("-------------------------------------------------")
            
        try:
            opcion = int(input("Ingrese el numero de la operacion que desea realiza:").strip())
            if opcion not in [0,1,2,3,4,5]:
                raise ValueError("Ingrese un valor de las opciones por favor :)")
        
        except ValueError as e:
            print(e)
            print("Intente de nuevo, por favor")
            continue

        if(opcion == 1):
            limpiar()
            print("Horarios del medico\n")
            cedulaDoctor = input("Ingrese la cedula del medico: ").strip()
            cita = Citas("","","","","","","")
            cita.ConsultarHorarioMedico(listaCitas, cedulaDoctor)

        if(opcion == 2):
            limpiar()
            print("Consultar fecha del paciente\n")
            cedulaPaciente = input("Ingrese la cedula del paciente: ").strip()
            cita = Citas("","","","","","","")
            cita.ConsultarFechaPaciente(listaCitas, cedulaPaciente)

        if(opcion == 3):
            limpiar()
            print("---------------------------------------")
            print("Informacion del medico")
            info = input("Ingrese la cedula del paciente :").strip()
            medi.InfoMedico(ListaMedicos,info)

        if(opcion == 4):
            limpiar()
            print("Medicos disponibles\n")
            Medicos.MedicosDisponibles(ListaMedicos)

        if(opcion == 5):
            limpiar()
            Pacientes.ImprimirLista(listaPacientes)

        if(opcion == 0):
            limpiar()
            break

def limpiar():
    if os.name == 'nt':
        os.system("cls")


#se saco paci de agregar datos, porque tiraba un error el infoPaciente
def MenuInicial(listaPacientes,listaCitas,listaMedicos):
    while True:
        print("--------Salud Connect------------------------")
        print("--------------------------------------------------------------")
        print("1. Administracion.",
              "\n2. Doctor.",
              "\n0. Salir.")
        print("--------------------------------------------------------------")    
        try:
            opcion = int(input("Ingrese el numero de la operacion que desea realiza:").strip())
            if opcion not in [0,1,2]:
                raise ValueError("Ingrese un valor de las opciones por favor :)")
        
        except ValueError as e:
            print(e)
            print("Intente de nuevo, por favor")
            continue

        if(opcion == 1):
            limpiar()
            print("----------------------")
            print("Bienvenido al sistema Salud Connect - Administracion")
            print("Por favor ingresar el usuario y contraseña correcto para ingresar :)")
            usuario = str(input("Usuario: ").strip().lower())
            contrasenia = str(input("Contraseña: ").strip().lower())
            if usuario == 'axel' and contrasenia == '111':
                limpiar()
                main_menu(listaPacientes,listaCitas,listaMedicos)
                break
            else:
                print("Contraseña incorrecta")
        if(opcion == 2):
            limpiar()
            print("----------------------")
            print("Bienvenido al sistema Salud Connect - Doctor")
            print("Por favor ingresar el usuario y contraseña correcto para ingresar :)")
            usuario = str(input("Usuario: ").strip().lower())
            contrasenia = str(input("Contraseña: ").strip().lower())
            if usuario == 'doctor1' and contrasenia == 'doctor11':
                menuDoctor(listaPacientes,listaCitas,listaMedicos)
            else:
                print("Contraseña incorrecta")

        if(opcion == 0):
            limpiar()
            print("Salir\n")
            print("Muchas gracias por ingresar y usar el sistema :) ")
            break

if __name__ == "__main__":
    listaPacientes = []
    listaCitas = []
    listaMedicos = []
    contador = 0
    while contador <=2:
        MenuInicial(listaPacientes,listaCitas,listaMedicos)
        contador +=1

#Muchas gracias - nos llevo demasiado esfuerza y cabeza, pero funca
#Pontifica universidad catolica del Ecuador Manabí - Primer semestre s1/2024 :)