from discord.ext import commands
from discord.commands import slash_command
import random
import discord

class VerifyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @discord.guild_only()
    async def verify(self, ctx):
        generation = generate()
        task = generation[1]
        result = generation[0]

        
        modal = VerifyModal(title="Verifiziere dich!", task=task, result=result)
        await ctx.send_modal(modal)

def setup(bot):
    bot.add_cog(VerifyCommand(bot))
    
    
def generate():
        numb_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        random_numb_1 = random.choice(numb_list)
        random_numb_2 = random.choice(numb_list)
        
        op = random.randint(1, 3)
        if op == 1:
            result = random_numb_1 + random_numb_2
            text = f"{random_numb_1} + {random_numb_2}"
        elif op == 2:
            result = random_numb_1 - random_numb_2
            text = f"{random_numb_1} - {random_numb_2}"
        elif op == 3:
            result = random_numb_1 * random_numb_2
            text = f"{random_numb_1} * {random_numb_2}"
            
        return [result, text]
    
class VerifyModal(discord.ui.Modal):
    def __init__(self, task, result, *args, **kwargs):
        
        self.result = result
        
        super().__init__(
            discord.ui.InputText(
                label=f"Berechne Folgende Aufgabe: {task}",
                placeholder="Ergebnis",
                
            ),
            
            *args,
            **kwargs
            )
        
    async def callback(self, interaction):
        try:
            if int(self.children[0].value) == self.result:
                await interaction.response.send_message("Du hast die Aufgabe richtig beantwortet", ephemeral=True)
                role = interaction.guild.get_role(1091780450059558972)
                await interaction.user.add_roles(role)
                
            elif int(self.children[0].value) != self.result:
                await interaction.response.send_message("Du hast die Aufgabe nicht richtig beantwortet", ephemeral=True)

                
        except:
            pass
            
        
