from models.video import Video
from models.podcast import Podcast
from models.textoNarrado import Texto_Narrado
from repositories.plataforma import Plataforma

video1 = Video("Curso Python", 40, "1080p")
podcast1 = Podcast("Roberto Cabrine",200,"Igão e Mitico")
TextoNarrado1 = Texto_Narrado("Programação facil",180,"Portugues")

plataforma = Plataforma("StreamX64")

plataforma.adicionar_midia(video1)
plataforma.adicionar_midia(podcast1)
plataforma.adicionar_midia(TextoNarrado1)

plataforma.listar_midias()

plataforma.reproduzir_todas()