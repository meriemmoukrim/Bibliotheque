from datetime import date,datetime

class Support :

    def __init__(self,id = str,titre = str,disponibilite = bool):
        self.__id = id
        self.__titre = titre
        self.__disponibilite = disponibilite

    @property
    def id(self):
        return  self.__id

    @id.setter
    def id(self,nouveauId):
           self.__id = nouveauId

    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self,nouveauTitre):

    @property
    def disponibilite(self):
        return  self.__disponibilite

    @disponibilite.setter
    def disponibilite(self,nouvelleDispo):
       if isinstance(nouvelleDispo ,int ):
           self.__disponibilite = nouvelleDispo
       else :
           raise ValueError("la disponibilité est invalide !!")

    def Verification(self):
        if   self.__disponibilite is not None:
            return ("le support disponible")
        else :
            return ("le support n'est pas disponible")

    def Rendre_Disponible(self):
      return   self.__disponibilite == True

    def Rendre_Non_Disponible(self):
        return self.__disponibilite == False

class Livre(Support):

    def __init__(self,id = str,titre = str,disponibilite = bool , auteur = str , Nb_Page = int):
        super().__init__(id = str,titre = str,disponibilite = bool)
        self.__auteur = auteur
        self.__Nb_Page = Nb_Page

    @property
    def auteur(self):
        return  self.__auteur

    @auteur.setter
    def auteur(self,nouveauAuteur):
        self.__auteur = nouveauAuteur

    @property
    def Nb_Page(self):
        self.__Nb_Page

    @Nb_Page.setter
    def Nb_Page(self,NouveauNb_Page):
        if NouveauNb_Page > 0:
            self.__Nb_Page=NouveauNb_Page
        else :
            raise ValueError(" nombre de page doit etre positive .")

class CD_ROM(Support):

      def __init__(self,id = str,titre = str,disponibilite = bool , capacite = int , editeur = str):
          super().__init__(id=str, titre=str, disponibilite=bool)
          self.__capacite = capacite
          self.__editeur = editeur

      @property
      def capacite(self):
          return self.__capacite

      @capacite.setter
      def capacite(self, nouveauCapacite):
          if nouveauCapacite > 0:
             self.__auteur = nouveauCapacite
          else:
              raise ValueError(" la capacité doit etre positive .")

      @property
      def editeur(self):
          return self.__editeur

      @editeur.setter
      def editeur(self, nouveauEditeur):
          self.__editeur = nouveauEditeur


class Magazine(Support):

    def __init__(self,id = str,titre = str,disponibilite = bool , NumeroPublic = int , datePublication = str):
        super().__init__(id=str, titre=str, disponibilite=bool)
        self.__NumeroPublic = NumeroPublic
        self.__datePublication = datePublication

    @property
    def NumeroPublic(self):
        return self.__NumeroPublic

    @NumeroPublic.setter
    def NumeroPublic(self, nouveauNumeroPublic):
        self.__NumeroPublic = nouveauNumeroPublic

    @property
    def datePublication (self):
        return self.__datePublication

    @datePublication .setter
    def datePublication (self, nouveau_Date_Publication ):
        if isinstance(nouveau_Date_Publication , date):
           self.__datePublication  = nouveau_Date_Publication
        else :
            raise ValueError(" la date de publication est invalid !!!")

class Adherent :

    def __init__(self,nom,prenom):
        self.__nom = nom
        self.__prenom = prenom

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self,nouvelleNom):
        self.__nom = nouvelleNom

    @property
    def prenom(self):
        return self.__nom

    @prenom.setter
    def nom(self, nouvellePrenom):
        self.__prenom = nouvellePrenom

class Emprunt():

    __auto = 0
    def __init__(self , adhernt ,supportEmp , dateEmprunt , dateRetour):
        Emprunt.__auto += 1
        self.__numeroEmprunt = Emprunt.__auto
        self.__adhernt = adhernt
        self.__supportEmp = supportEmp
        self.__dateEmprunt = dateEmprunt
        self.__dateRetour = dateRetour

    @property
    def numeroEmprunt(self):
        self.__numeroEmprunt

    @property
    def adhernt(self):
        self.__adhernt

    @adhernt.setter
    def adhernt(self,nouvelleAdhernt):
        self.__adhernt = nouvelleAdhernt

    @property
    def supportEmp(self):
        self.__supportEmp

    @supportEmp .setter
    def supportEmp (self, nouvelleSupportEmp ):
        self.__supportEmp = nouvelleSupportEmp


    @property
    def dateEmprunt(self):
        return self.__dateEmprunt

    @dateEmprunt.setter
    def dateEmprunt(self, nouveau_Date_Emprunt):
        if isinstance(nouveau_Date_Emprunt, date):
            self.__dateEmprunt = nouveau_Date_Emprunt
        else:
            raise ValueError(" la date Emprunt est invalid !!!")

    @property
    def dateRetour(self):
        return self.__dateRetour

    @dateRetour.setter
    def dateRetour(self, nouveau_Date_Retour):
        if isinstance(nouveau_Date_Retour, date):
            self.__dateRetour = nouveau_Date_Retour
        else:
            raise ValueError(" la date de publication est invalid !!!")

    def Marquer_Support_Comme_Emprunte(self):
        if  self.__dateRetour is not None :
            return True
        return self.__dateRetour > datetime.date.today()

    def Marquer_Support_Comme_Rendu(self):
        if


    def Afficher_details(self):
        print(f"Numero Emprunt : {self.__numeroEmprunt}\n"
              f"Adhernt : {self.__adhernt}\n"
              f"supportEmp : {self.__supportEmp}\n"
              f"dateEmprunt : {self.__dateEmprunt}\n"
              f"dateRetour : {self.__dateRetour}")



















