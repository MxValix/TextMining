# librerie per connettermi al database postgres 
library(DBI)
library(RPostgreSQL)
library(odbc)

# variabili per connessione al db
db_driver <- dbDriver("PostgreSQL")
db_name <- 'textmining'
db_host <- 'localhost'
db_port <- 5432
db_user <- 'postgres'
db_password <- "admin"

# connessione al db
connessione <- dbConnect( db_driver, 
                          dbname= db_name, 
                          host= db_host, 
                          port= db_port, 
                          user = 'postgres',
                          password=  db_password )
# per controllare se la connessione è stata stabilita
# dbConnect(connessione)

# importo i dati dal mio documento excel
textmining <- read_excel("textmining.xlsx")

# creo una tabella nel db con i dati del mio dataset
dbWriteTable(connessione, "WomenClothing", textmining)

# leggo i dati dalla tabella del database
data <- dbReadTable(connessione, "WomenClothing")
View(data)

# recupero e mostro tutti i dati il cui rating < 3
# badRating <- subset(data, Rating < 3)
# View(badRating)

# estraggo  un elenco degli id dalla colonna clothing.id scremando i doppioni 
distinct_id <- unique(data$Clothing.ID)
d_len <- length(distinct_id)
View(distinct_id)

# dichiaro ed inizializzo distinct
distinct <- data.frame(Clothing.ID = numeric(), Rating = numeric(), Eta = numeric())

# scorro distinct_id
for (d in distinct_id){
  # per ogni distinct_id salvo nella stessa variabile tutti i record con lo stesso id
  tmp <- subset(data, Clothing.ID == d)
  # salvo in una variabile l'id corrispondente 
  clothingId <- unique(tmp$Clothing.ID)
  # salvo la media rating corrispondente all'id
  mediaRating <- mean(tmp$Rating)
  # salvo la media età corrispondente all'id
  mediaAge <- mean(tmp$Age)
  # metto nel dataframe il record corrente, costituito da id, media rating e media età
  distinct <- rbind(distinct,data.frame(clothingid,mediaRating,mediaAge))
}
#names(distinct)[1] <- "Clothing.ID"
#names(distinct)[2] <- "Rating"
#names(distinct)[3] <- "Age"

# ordino il dataframe in base alla media rating (da 1 a 5)
distinct <- distinct[order(distinct[2]),]
# creo la tabella distinctClothing a cui passo il dataframe distinct
dbWriteTable(connessione,"distinctClothing", distinct)
# leggo la tabella distinctClothing
distinct <- dbReadTable(connessione,"distinctClothing")
View(distinct)
