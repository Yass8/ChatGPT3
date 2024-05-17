from openai import OpenAI
client = OpenAI(api_key="")

import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

class requestsAPP(customtkinter.CTk):
    user_input = ""
    user_input_param = ""
    historique_conversation = [{'role': 'system', 'content': 'Tu repondras par la négation à toutes les questions que ton interlocuteur te pose'}]

    def __init__(self):
        super().__init__()
        self.title("Mon application #1")
        self.geometry(f"{1100}x{580}")

        # créer une grille de 3 lignes et 3 colonnes
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # partie bouton
        self.buton_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.buton_frame.grid(row=0, column=1, sticky="w")

        self.button = customtkinter.CTkButton(master=self.buton_frame, text="Envoyer",height=40, command=self.update_user_input)
        self.button.grid()

        # partie champs texte
        self.text_frame = customtkinter.CTkFrame(self, width=800, corner_radius=0)
        self.text_frame.grid(row=0, column=0)

        self.user_text = customtkinter.CTkEntry(master=self.text_frame, placeholder_text="Message à ChatGpt",height=40, width=800)
        self.user_text.grid()

        # partie paramètre système
        self.text_frame2 = customtkinter.CTkFrame(self, width=10, corner_radius=0)
        self.text_frame2.grid(row=1, column=1, sticky="n")

        self.user_text2 = customtkinter.CTkEntry(master=self.text_frame2, placeholder_text="Paramètre système", height=40, width=260)
        self.user_text2.grid()

        # partie bouton paramètre
        self.buton_frame2 = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.buton_frame2.grid(row=1, column=1, padx=20, pady=50, sticky="n")

        self.button2 = customtkinter.CTkButton(master=self.buton_frame2, text="Sauvegarder le paramètre", command=self.update_user_param)
        self.button2.grid()


        # partie slider
        def slider_event(value):
            self.slider_label.configure(text=f"Valeur de la temperature : {value}")

        self.slider = customtkinter.CTkSlider(self, from_=0, to=2, command=slider_event)
        self.slider.grid(row=1, column=1)

        self.slider_label = customtkinter.CTkLabel(self, text=f"Valeur de la temperature : {self.slider.get()}")
        self.slider_label.grid(row=1, column=1, padx=20, pady=190, sticky="s")

        

        # partie resultat
        self.result_frame = customtkinter.CTkFrame(self, width=800, corner_radius=0)
        self.result_frame.grid(row=1, column=0, sticky="n")

        self.result_box = customtkinter.CTkTextbox(master=self.result_frame, height=400, width=800)
        self.result_box.configure(state="disabled")
        self.result_box.grid(sticky="nsew")

    def update_user_input(self):
        self.result_box.configure(state="normal")
        self.result_box.delete("0.0", "end")
        
        # récupere le texte de l'utilisateur
        t = self.user_text.get()
        self.user_input = t
        self.historique_conversation.append({'role': 'user', 'content': self.user_input})

        # appeler l'API OpenAI
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.historique_conversation,
                temperature= self.slider.get(),
                max_tokens=1000
            )
            response = completion.choices[0].message.content
            self.historique_conversation.append({'role': 'assistant', 'content': response})
        except Exception as e:
            response = "Erreur lors de la requête"

        # mettre à jour l'affichage de l'historique comme un dialogue
        dialogue = ""
        for message in self.historique_conversation:
            role = message['role']
            content = message['content']
            if role != 'system':  # Exclure les messages de type 'system'
                dialogue += f"{role.capitalize()}: {content}\n\n"

        self.result_box.insert("0.0", dialogue)
        self.result_box.configure(state="disabled")

    def update_user_param(self):
        self.result_box.configure(state="normal")
        self.result_box.delete("0.0", "end")

        text_param = self.user_text2.get()
        self.user_input_param = text_param
        self.historique_conversation[0]['content'] = self.user_input_param
        print(self.historique_conversation[0]['content'])

if __name__ == "__main__":
    mon_instance = requestsAPP()
    mon_instance.mainloop()
