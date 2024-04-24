import folium

# Criar um mapa centrado em uma localização específica
mapa = folium.Map(location=[-22.9068, -43.1729], zoom_start=12)

# Adicionar marcador
folium.Marker([-22.9068, -43.1729], popup='Rio de Janeiro').add_to(mapa)

# Salvar o mapa como um arquivo HTML
mapa.save('mapa.html')
