<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta name="description" content="">
		<meta name="author" content="">
		<link rel="shortcut icon" href="themes/assets/ico/favicon.ico">

		<link href="themes/dist/css/bootstrap.min.css" rel="stylesheet">

		<link href="themes/assets/css/carousel.css" rel="stylesheet">
		<script type="text/javascript" src="http://maps.google.com/maps/api/js?key=AIzaSyCuzPAK5WOrN0iFst9sLiuhBZisZcDTcMM"></script>
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/angularjs/1.0.3/angular.min.js"></script>
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
	</head>
	<!-- NAVBAR
	================================================== -->
	<body>
		<div class="navbar-wrapper">
			<div class="container">

				<div class="navbar navbar-inverse navbar-static-top" role="navigation">
					<div class="container">
						<div class="navbar-header">
							<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
								<span class="sr-only">Toggle navigation</span>
								<span class="icon-bar"></span>
								<span class="icon-bar"></span>
								<span class="icon-bar"></span>
							</button>
							<a class="navbar-brand" href="index.html">Stiv</a>
						</div>
						<div class="navbar-collapse collapse">
							<ul class="nav navbar-nav">
								<li>
									<form action="index-test.php" method="get">
									<p>Cochez les catégories recherchées:</p>
										<p>
										<input type="checkbox" name="ville" value="Paris">Paris<br>
										<input type="checkbox" name="ville" value="Marseille">Marseille<br>
										<input type="checkbox" name="categorie" value="Restaurant">Restaurant<br>
										<input type="checkbox" name="categorie" value="Shopping">Shopping<br>
										<input type="submit" value="Rechercher"/>
										</p>
									</form>
								</li>
							</ul>
						</div>
					</div>
				</div>

			</div>
		</div>

		<!-- Carousel
		================================================== -->
		<div id="mainCarousel">
			<div id="myCarousel" class="carousel slide" data-ride="carousel">
				<!-- Indicators -->
				<ol class="carousel-indicators">
					<li data-target="#myCarousel" data-slide-to="0" class="active"></li>
					<li data-target="#myCarousel" data-slide-to="1"></li>
					<li data-target="#myCarousel" data-slide-to="2"></li>
				</ol>
				<div class="carousel-inner">
					<div class="item active">
						<div id="googleMap" style="height:750px;"></div>

	<?php
	// Accès à la base de données
	$connexion = new mysqli("localhost", "root", "", "stiv") or die(mysqli_error());

	if(mysqli_connect_errno())
	{
		echo"Failde to connect to MySQL: ".mysqli_connect_error();
	}
	//SQL statement sélection des données
	$result = $connexion->query("SELECT categorie,city,latitude,longitude FROM test order by id");
	$items = array();
	WHILE ($row = $result->fetch_object())
	{
    	// Ecriture des données sous format JSON
    	$items[] = array('categorie'=>$row->categorie, 'city'=>$row->city, 'latitude'=>(float)$row->latitude, 'longitude'=>(float)$row->longitude);
    	//$items[] = array('name'=>$row->name);
    	//printf("%s %f %f\n", $row->name, $row->latitude, $row->longitude);
	}
	mysqli_free_result($result);

	//Encodage en JSON
	$json = json_encode($items);
	$error = json_last_error();
	var_dump($json);
	echo '<br>erreur : '.$error;

	//Fermeture connection
	mysqli_close($connexion);
	echo $json
	?>

						<script type="text/javascript">

						function $_GET(param) {
	var vars = {};
	window.location.href.replace( location.hash, '' ).replace(
		/[?&]+([^=&]+)=?([^&]*)?/gi, // regexp
		function( m, key, value ) { // callback
			vars[key] = value !== undefined ? value : '';
		}
	);

	if ( param ) {
		return vars[param] ? vars[param] : null;
	}
	return vars;
}

var $_GET = $_GET(),
    ville_r = $_GET['ville_r'],
    ville = $_GET['ville'];
    categorie_r = $_GET['categorie_r'];
    categorie = $_GET['categorie'];
    //alert(ville_r);
    alert(ville);
    alert(categorie);
							var map = new google.maps.Map(document.getElementById("googleMap"), {
								zoom: 12,
								center: new google.maps.LatLng(48.858565, 2.347198),
								//mapTypeId: google.maps.MapTypeId.ROADMAP
							});

							if (navigator.geolocation)
  var watchId = navigator.geolocation.watchPosition(successCallback,
                            null,
                            {enableHighAccuracy:true});
else
  alert("Votre navigateur ne prend pas en compte la géolocalisation HTML5");

function successCallback(position){
  map.panTo(new google.maps.LatLng(position.coords.latitude, position.coords.longitude));
  var marker = new google.maps.Marker({
    position: new google.maps.LatLng(position.coords.latitude, position.coords.longitude),
    map: map
  });


							function addMarker(latitude, longitude, title)
							{
								title = title || ''; // Si on n'a pas de titre, on ne met rien
								var marker = new google.maps.Marker({
									position: new google.maps.LatLng(latitude, longitude),
									animation: google.maps.Animation.DROP,
									title: title
								});
								marker.setMap(map);
							}
							addMarker();

	var json='<?php echo $json;?>';
    var data = JSON.parse(json);
	for(var i in data){
    			obj = data[i];
    			console.log(obj);
    			if((obj.city==ville)&&(obj.categorie==categorie)){
    				addMarker(obj.latitude, obj.longitude);
    			}

}
}


						</script>
						<div class="container">
						</div>
					</div>
				</div>
			</div><!-- /.carousel -->
		</div>

		<div class="mainTitle">
			<div class="container">
				<h1>Avec Stiv, recherchez tout ce que vous voulez !</h1>
				<p>
					Restaurants, bars, centres commerciaux, shopping, Stiv sélectionne ce qui vous correspond !
				</p>
			</div>
		</div>


	</body>
</html>
