import customtkinter as ctk
from mysql.connector import connect, Error
from decimal import Decimal

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "unifecaf",
    "database": "Loja_Jogos"
}

def conectar_banco():
    try:
        return connect(**DB_CONFIG)
    except Error as e:
        mostrar_mensagem(f"Erro ao conectar ao MySQL: {e}", cor="#FF5555")
        return None

def listar_produtos_db():
    conn = conectar_banco()
    produtos = []
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
            SELECT p.pro_id, p.pro_nome, p.prod_desc, p.prod_preco, p.qntd_estoque
            FROM tb_produtos p
            ORDER BY p.pro_nome
            """
            cursor.execute(query)
            produtos = cursor.fetchall()
        except Exception as e:
            mostrar_mensagem(f"Erro ao listar produtos: {e}", cor="#FF5555")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if conn:
                conn.close()
    return produtos

def adicionar_produto_db(nome, descricao, preco, estoque):
    conn = conectar_banco()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            INSERT INTO tb_produtos
            (pro_nome, prod_desc, prod_preco, qntd_estoque, cat_id, forn_id)
            VALUES (%s, %s, %s, %s, 1, 1)
            """
            cursor.execute(query, (nome, descricao, preco, estoque))
            conn.commit()
            return True
        except Exception as e:
            mostrar_mensagem(f"Erro ao adicionar produto: {e}", cor="#FF5555")
            return False
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if conn:
                conn.close()
    return False

def atualizar_produto_db(produto_id, nome, descricao, preco, estoque):
    conn = conectar_banco()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            UPDATE tb_produtos
            SET pro_nome = %s, prod_desc = %s, prod_preco = %s, qntd_estoque = %s
            WHERE pro_id = %s
            """
            cursor.execute(query, (nome, descricao, preco, estoque, produto_id))
            conn.commit()
            return True
        except Exception as e:
            mostrar_mensagem(f"Erro ao atualizar produto: {e}", cor="#FF5555")
            return False
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if conn:
                conn.close()
    return False

def remover_produto_db(produto_id):
    conn = conectar_banco()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tb_produtos WHERE pro_id = %s", (produto_id,))
            conn.commit()
            return True
        except Exception as e:
            mostrar_mensagem(f"Erro ao remover produto: {e}", cor="#FF5555")
            return False
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if conn:
                conn.close()
    return False

def atualizar_lista_jogos(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    produtos = listar_produtos_db()
    root = frame.winfo_toplevel()
    
    for prod in produtos:
        # Frame para cada item
        item_frame = ctk.CTkFrame(frame, fg_color="transparent")
        item_frame.pack(fill="x", pady=2, padx=2)
        
        texto = f"{prod['pro_nome']} | R${prod['prod_preco']:.2f} | Estoque: {prod['qntd_estoque']}\n{prod['prod_desc']}"
        label = ctk.CTkLabel(
            item_frame, 
            text=texto, 
            anchor="w", 
            justify="left", 
            font=("Arial", 12), 
            text_color="#fff"
        )
        label.pack(fill="x", pady=2, padx=2)
        
        # Função para selecionar item
        def make_click_handler(pid, label_widget):
            def click_handler(e):
                # Resetar cores de todos os itens
                for widget in frame.winfo_children():
                    for child in widget.winfo_children():
                        if isinstance(child, ctk.CTkLabel):
                            child.configure(fg_color="transparent", text_color="#fff")
                
                # Destacar item selecionado
                label_widget.configure(fg_color="#3a4149", text_color="#FFD700")
                root.selected_id = pid
                print(f"Selecionado: ID {pid}")
            return click_handler
        
        # Bind click event
        label.bind("<Button-1>", make_click_handler(prod['pro_id'], label))
        item_frame.bind("<Button-1>", make_click_handler(prod['pro_id'], label))

def mostrar_mensagem(msg, cor="#FFD700"):
    for widget in modify_frame.winfo_children():
        if getattr(widget, 'is_msg', False):
            widget.destroy()
    label = ctk.CTkLabel(modify_frame, text=msg, text_color=cor, font=("Arial", 12))
    label.is_msg = True
    label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

def limpar_modify_frame():
    for widget in modify_frame.winfo_children():
        widget.destroy()

def exibir_form_adicionar():
    limpar_modify_frame()
    ctk.CTkLabel(modify_frame, text="Adicionar Jogo", font=("Arial Black", 16), text_color="#FFD700").pack(pady=(10,5))
    nome_entry = ctk.CTkEntry(modify_frame, placeholder_text="Nome do Jogo")
    nome_entry.pack(pady=5, fill="x", padx=20)
    desc_entry = ctk.CTkEntry(modify_frame, placeholder_text="Descrição")
    desc_entry.pack(pady=5, fill="x", padx=20)
    preco_entry = ctk.CTkEntry(modify_frame, placeholder_text="Preço (R$)")
    preco_entry.pack(pady=5, fill="x", padx=20)
    estoque_entry = ctk.CTkEntry(modify_frame, placeholder_text="Estoque")
    estoque_entry.pack(pady=5, fill="x", padx=20)
    def salvar():
        nome = nome_entry.get().strip()
        desc = desc_entry.get().strip()
        try:
            preco = Decimal(preco_entry.get().replace(",", "."))
            estoque = int(estoque_entry.get())
        except Exception:
            mostrar_mensagem("Preço e Estoque inválidos.", cor="#FF5555")
            return
        if nome:
            if adicionar_produto_db(nome, desc, preco, estoque):
                atualizar_lista_jogos(scrollable_frame)
                mostrar_mensagem("Jogo adicionado com sucesso!", cor="#44FF44")
                limpar_modify_frame()
            else:
                mostrar_mensagem("Erro ao adicionar.", cor="#FF5555")
        else:
            mostrar_mensagem("Nome obrigatório.", cor="#FF5555")
    # Frame horizontal para os botões
    botoes_frame = ctk.CTkFrame(modify_frame, fg_color="transparent")
    botoes_frame.pack(pady=10)
    ctk.CTkButton(botoes_frame, text="Salvar", command=salvar, width=120).pack(side="left", padx=(0, 10))
    ctk.CTkButton(botoes_frame, text="Cancelar", command=limpar_modify_frame, width=120).pack(side="left")

def exibir_form_editar():
    root = scrollable_frame.winfo_toplevel()
    if not hasattr(root, 'selected_id') or not root.selected_id:
        mostrar_mensagem("Selecione um jogo na lista.", cor="#FF5555")
        return
    produto_id = root.selected_id
    conn = conectar_banco()
    prod = None
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM tb_produtos WHERE pro_id = %s", (produto_id,))
            prod = cursor.fetchone()
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if conn:
                conn.close()
    if not prod:
        mostrar_mensagem("Produto não encontrado.", cor="#FF5555")
        return
    limpar_modify_frame()
    ctk.CTkLabel(modify_frame, text=f"Editar Jogo (ID {produto_id})", font=("Arial Black", 16), text_color="#FFD700").pack(pady=(10,5))
    nome_entry = ctk.CTkEntry(modify_frame)
    nome_entry.insert(0, prod['pro_nome'])
    nome_entry.pack(pady=5, fill="x", padx=20)
    desc_entry = ctk.CTkEntry(modify_frame)
    desc_entry.insert(0, prod['prod_desc'])
    desc_entry.pack(pady=5, fill="x", padx=20)
    preco_entry = ctk.CTkEntry(modify_frame)
    preco_entry.insert(0, f"{prod['prod_preco']:.2f}")
    preco_entry.pack(pady=5, fill="x", padx=20)
    estoque_entry = ctk.CTkEntry(modify_frame)
    estoque_entry.insert(0, str(prod['qntd_estoque']))
    estoque_entry.pack(pady=5, fill="x", padx=20)
    def salvar():
        nome = nome_entry.get().strip()
        desc = desc_entry.get().strip()
        try:
            preco = Decimal(preco_entry.get().replace(",", "."))
            estoque = int(estoque_entry.get())
        except Exception:
            mostrar_mensagem("Preço e Estoque inválidos.", cor="#FF5555")
            return
        if nome:
            if atualizar_produto_db(produto_id, nome, desc, preco, estoque):
                atualizar_lista_jogos(scrollable_frame)
                mostrar_mensagem("Jogo atualizado!", cor="#44FF44")
                limpar_modify_frame()
            else:
                mostrar_mensagem("Erro ao atualizar.", cor="#FF5555")
        else:
            mostrar_mensagem("Nome obrigatório.", cor="#FF5555")
    # Frame horizontal para os botões
    botoes_frame = ctk.CTkFrame(modify_frame, fg_color="transparent")
    botoes_frame.pack(pady=10)
    ctk.CTkButton(botoes_frame, text="Salvar", command=salvar, width=120).pack(side="left", padx=(0, 10))
    ctk.CTkButton(botoes_frame, text="Cancelar", command=limpar_modify_frame, width=120).pack(side="left")

def remover_jogo():
    root = scrollable_frame.winfo_toplevel()
    if not hasattr(root, 'selected_id') or not root.selected_id:
        mostrar_mensagem("Selecione um jogo na lista.", cor="#FF5555")
        return
    produto_id = root.selected_id
    if remover_produto_db(produto_id):
        atualizar_lista_jogos(scrollable_frame)
        root.selected_id = None
        mostrar_mensagem("Jogo removido!", cor="#44FF44")
    else:
        mostrar_mensagem("Erro ao remover.", cor="#FF5555")

def main():
    global scrollable_frame, modify_frame
    root = ctk.CTk()
    root.geometry("800x750")  # Aumentado para melhor visualização
    root.title("Loja de Jogos")
    root.resizable(False, False)
    root.configure(fg_color="#23272F")
    root.selected_id = None
    # Função para atualizar o ID selecionado
    def set_selected_id(pid):
        root.selected_id = pid
        print(f"Jogo selecionado: ID {pid}")  # Feedback visual no console
    root.set_selected_id = set_selected_id

    # Quadro com título - Centralizado e maior
    title_frame = ctk.CTkFrame(root, fg_color="#1a1d23", corner_radius=15, width=750, height=70)
    title_frame.place(relx=0.5, y=15, anchor="n")
    title_frame.pack_propagate(False)
  
    title_label = ctk.CTkLabel(
        title_frame,
        text="🎮 LOJA DE JOGOS",
        font=("Arial Black", 24, "bold"),
        text_color="#FFD700"
    )
    title_label.place(relx=0.5, rely=0.5, anchor="center")
  
    # Frame para os botões - Melhor organizado
    button_frame = ctk.CTkFrame(root, fg_color="transparent", width=200, height=300)
    button_frame.place(x=30, y=100)

    add_button = ctk.CTkButton(
        button_frame, 
        text="ADICIONAR JOGO", 
        command=exibir_form_adicionar, 
        width=180, 
        height=50,
        font=("Arial Bold", 14)
    )
    add_button.pack(pady=10)

    edit_button = ctk.CTkButton(
        button_frame, 
        text="EDITAR JOGO", 
        command=exibir_form_editar, 
        width=180, 
        height=50,
        font=("Arial Bold", 14)
    )
    edit_button.pack(pady=10)

    remove_button = ctk.CTkButton(
        button_frame, 
        text="REMOVER JOGO", 
        command=remover_jogo, 
        width=180, 
        height=50,
        font=("Arial Bold", 14)
    )
    remove_button.pack(pady=10)

    # Quadro com lista de jogos
    scrollable_frame = ctk.CTkScrollableFrame(
        root, 
        width=520, 
        height=300,
        fg_color="#1a1d23",
        corner_radius=10
    )
    scrollable_frame.place(x=230, y=100)
    atualizar_lista_jogos(scrollable_frame)

    # Quadro de modificação
    modify_frame = ctk.CTkFrame(
        root, 
        fg_color="#1a1d23", 
        corner_radius=15, 
        width=740, 
        height=250
    )
    modify_frame.place(relx=0.5, y=470, anchor="n")
    modify_frame.pack_propagate(False)

    root.mainloop()

if __name__ == "__main__":
    main()
