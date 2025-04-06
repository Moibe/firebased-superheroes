import inputs
import globales
import funciones
import sulkuFront
import gradio as gr
import firehead, fire, fuego 

def iniciar():    
    app_path = globales.app_path
    main.queue(max_size=globales.max_size)
    main.launch(root_path=app_path, server_port=globales.server_port)

#Credit Related Elements
html_credits = gr.HTML(visible=globales.credits_visibility)
lbl_console = gr.Label(label="AI Terminal " + globales.version +  " messages", value="Hola", container=True)
btn_buy = gr.Button("Get Credits", visible=False, size='lg')

#Customizable Inputs and Outputs
input1, gender, hero, result = inputs.inputs_selector(globales.seto)  

#Otros Controles y Personalizaciones
nombre_posicion = gr.Label(label="Posición", visible=globales.posicion_marker)

#fire provee las partes de javascript que se requieren para correr el chequeo de firebase.
with gr.Blocks(theme=globales.tema, head=firehead.head, js=fire.js, css="footer {visibility: hidden}") as main: 

    
    usuario_local = gr.Textbox(visible=False) #Para almacenar el usuario de firebase 
    main.load(sulkuFront.precarga, usuario_local, [html_credits, usuario_local], js=fuego.js) if globales.acceso != "libre" else None
       
    with gr.Row():
        demo = gr.Interface(
            fn=funciones.perform,
            inputs=[input1, gender, hero, usuario_local], 
            outputs=[result, lbl_console, html_credits, btn_buy, nombre_posicion], 
            flagging_mode=globales.flag
            )
iniciar()