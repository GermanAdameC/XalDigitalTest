--Respuestas:
--Numero 1:
select nombre(
  select max(counter), nombre from (
    select vuelos.ID_AEROPUERTO, count(vuelos.ID_AEROPUERTO) as counter, aeropuertos.NOMBRE_AEROPUERTO as nombre 
    from vuelos join aeropuertos on vuelos.ID_AEROPUERTO = aeropuertos.ID_AEROPUERTO group by vuelos.ID_AEROPUERTO
  )
);

--Numero 2:
select nombre from (select max(counter), nombre from (
    select vuelos.ID_AEROLINEA, count(vuelos.ID_AEROLINEA) as counter, aerolineas.NOMBRE_AEROLINEA as nombre
    from vuelos join aerolineas where vuelos.ID_MOVIMIENTO = 1 and vuelos.ID_AEROLINEA =  aerolineas.ID_AEROLINEA 
    group by Orders.vuelos.ID_AEROLINEA
)
);

--Numero 3:
select DIA from (select max(counter), DIA from (
    select DIA, count(DIA) as counter from vuelos where ID_MOVIMIENTO = 1 
    group by DIA
    )
);

--Numero 4:
select nombre from (
    select vuelos.ID_AEROLINEA, count(distinct(vuelos.DIA)) as counter, aerolineas.NOMBRE_AEROLINEA as nombre 
    from vuelos join aerolineas on vuelos.ID_MOVIMIENTO = 1 and vuelos.ID_AEROLINEA = aerolineas.ID_AEROLINEA 
    group by vuelos.ID_AEROLINEA 
    having counter > 2
);
