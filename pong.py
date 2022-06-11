import pygame

class Main():
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Pong")

        self.fontti_pieni = pygame.font.SysFont("Segoe UI", 24, bold=True)
        self.fontti_suuri = pygame.font.SysFont("Segoe UI", 50, bold=True)

        self.leveys, self.korkeus = 640, 480
        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus))

        self.kello = pygame.time.Clock()

        self.lataa_kuvat()

        self.paikka1 = self.korkeus / 2 - self.kuvat[0].get_height() / 2
        self.paikka2 = self.korkeus / 2 - self.kuvat[1].get_height() / 2

        self.palloX, self.palloY = self.leveys / 2 - self.kuvat[2].get_width() / 2, self.korkeus / 2 - self.kuvat[2].get_height() / 2

        self.ylos1 = False
        self.alas1 = False

        self.ylos2 = False
        self.alas2 = False

        self.silmukka()

    def lataa_kuvat(self):
        self.kuvat = []
        for kuva in ["lauta1.png", "lauta2.png", "pallo.png"]:
            self.kuvat.append(pygame.image.load(kuva))

    def pelaaja1(self):
        if self.ylos1 and self.paikka1 > 0:
            self.paikka1 -= 5
        if self.alas1 and self.paikka1 <= self.korkeus - self.kuvat[0].get_height():
            self.paikka1 += 5

    def pelaaja2(self):
        if self.ylos2 and self.paikka2 > 0:
            self.paikka2 -= 5
        if self.alas2 and self.paikka2 <= self.korkeus - self.kuvat[1].get_height():
            self.paikka2 += 5

    #def pallo_liike(self):
        #self.palloY += 2
        #if self.palloY >= self.korkeus - self.kuvat[2].get_height():
            #self.palloY -= 2

    def lopetusnaytto(self):
        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_ESCAPE:
                        exit()

    def silmukka(self):
        while True:
            self.tapahtumat()
            self.piirra_naytto()

    def tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_UP:
                    self.ylos1 = True
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas1 = True
                if tapahtuma.key == pygame.K_w:
                    self.ylos2 = True
                if tapahtuma.key == pygame.K_s:
                    self.alas2 = True
                if tapahtuma.key == pygame.K_ESCAPE:
                    exit()

            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_UP:
                    self.ylos1 = False
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas1 = False
                if tapahtuma.key == pygame.K_w:
                    self.ylos2 = False
                if tapahtuma.key == pygame.K_s:
                    self.alas2 = False

            if tapahtuma.type == pygame.QUIT:
                exit()

    def piirra_naytto(self):

        self.naytto.fill((0, 0, 0))

        self.pelaaja1()
        self.pelaaja2()
        self.pallo_liike()

        self.naytto.blit(self.kuvat[0], (15, self.paikka1))
        self.naytto.blit(self.kuvat[1], (self.leveys - self.kuvat[1].get_width() - 15, self.paikka2))
        self.naytto.blit(self.kuvat[2], (self.palloX, self.palloY))

        pygame.display.flip()

        self.kello.tick(60)

if __name__ == "__main__":
    Main()

