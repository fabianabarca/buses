let current_route=null

let tripsData = RemoveSingleQuotes(document.getElementById("Trips").text)
let routesData = RemoveSingleQuotes(document.getElementById("Routes").text);
let rawShapesData = RemoveSingleQuotes(document.getElementById("Shapes").text)
let stopsData = RemoveSingleQuotes(document.getElementById("Stops").text);
let jsonLabels = RemoveSingleQuotes(document.getElementById("Labels").text)

rawShapesData = JSON.parse(rawShapesData)
stopsData = JSON.parse(stopsData);
tripsData = JSON.parse(tripsData)
routesData = JSON.parse(routesData);
jsonLabels = JSON.parse(jsonLabels);


let label = SetLabel(current_route, tripsData);
let shapesData = SetLabels(current_route, jsonLabels, stopsData, HandleShapes(rawShapesData, current_route));
let color = SetColor(current_route, tripsData.route_shape_id_relation, routesData);

console.log(label);
let myChart = document.getElementById("myChart");
let elevationChart = new Chart(myChart, {
  type:'line',
  data:{
    labels:shapesData.shape_pt_town,
    datasets:[
      {
      fill:true,
      label:label,
      data:MovingAvg(shapesData.shape_pt_alt, 5, function(val){return val != 0; }),
      backgroundColor:color.backgroundColor,
      borderWidth:1,
      borderColor:color.borderColor,
      hoverBorderWidth:3,
      hoverBorderColor:'#000',
    }
    ],
  },
  options:{
    scales:{
      y:{
        title:{
            color:'black',
            display:true,
            text:'Altitud (msnm)'
        },
        beginAtZero: false
      },
      x:{
        title:{
            color:'black',
            display:false,
            text:'Recorrido'
        },
        ticks:{
          display:true,
          autoskip:false,
          maxRotation: 90,
          minRotation: 90,
          callback:function(value, index, values) {
            if(this.getLabelForValue(value)!==""){
              return this.getLabelForValue(value);
            }
          }
        }
      }
  },
    plugins:{
      title:{
        display:true,
        text:'Elevation tracker',
        fontSize:25
      }
  },
    legend: {
        display:false
    }
    },
    elements:{
      line:{
        fill:true,
        tension:0.5,
        borderJoinStyle: 'miter',
        capBezierPoints: true
      }
    }
  });

function InitializeData(){
  let select = document.getElementById("selector_routes");
  if (select != null){
    let option = select.options[select.selectedIndex];
    current_route = option.value.split("|")[0]
    current_headsign = option.value.split("|")[1]
  }
  else{
    let current_route = null
  }
  label = SetLabel(current_route, tripsData,current_headsign);
  shapesData = SetLabels(current_route, jsonLabels, stopsData, HandleShapes(rawShapesData, current_route))
  color = SetColor(current_route, tripsData.route_shape_id_relation, routesData);
}
function ChangeRoute(){
  InitializeData()
  elevationChart.data.labels = shapesData.shape_pt_town
  elevationChart.data.datasets[0].data = MovingAvg(shapesData.shape_pt_alt, 25, function(val){return val != 0; })
  elevationChart.data.datasets[0].label = label
  elevationChart.data.datasets[0].backgroundColor = color.backgroundColor
  elevationChart.data.datasets[0].borderColor = color.borderColor

  elevationChart.update();
}
function RemoveSingleQuotes(data){
  return out = data.replace(/&quot;/g,'"');
}
function HandleShapes(data, current_route){
  let shape_pt_alt = []
  let shape_dist_traveled = []
  let shape_pt_lat = []
  let shape_pt_lon = []
  let shape_id = null
  //let stops = []
  if(data.length !== 0){
    for (let i=0; i < data.length; i++){
      shape_id = data[i].shape_id;
      if (shape_id === current_route){
        shape_pt_alt.push(parseFloat(data[i].shape_pt_alt));
        shape_dist_traveled.push(parseFloat(data[i].shape_dist_traveled));
        shape_pt_lat.push(data[i].shape_pt_lat);
        shape_pt_lon.push(data[i].shape_pt_lon);

        //stops.push(routeStops)
      }
    }
  }
return {
  shape_pt_alt,
  shape_dist_traveled,
  shape_pt_lat,
  shape_pt_lon
};
}
function HandleRoutes(data){
  let route_id = []
  let route_short_name = []
  let route_color = []
  if(data.length !== 0){
    for (let i=0; i < data.length; i++){
    //let route_id = (data[i].route_id);
    //let route_short_name = data[i].route_short_name;
    //let route_color = data[i].route_color;
    route_id.push(data[i].route_id);
    route_short_name.push(data[i].route_short_name);
    route_color.push(data[i].route_color)
  }
  }
return {
  route_id,
  route_short_name,
  route_color
};
}
function HandleTrips(data){
  let route_shape_id_relation = {};
  let headsign_shape_id_relation = {};
  if(data.length !== 0){
    for (let i=0; i < data.length; i++){
      let route_id = data[i].route_id;
      let shape_id = data[i].shape_id;
      let trip_headsign = data[i].trip_headsign;
      //console.log(data.length)
      //console.log(route_id)
      if(route_shape_id_relation.hasOwnProperty(route_id)===false){
        route_shape_id_relation[route_id] = [];
        route_shape_id_relation[route_id].push(shape_id);
      }
      else if((route_shape_id_relation.hasOwnProperty(route_id))
      &&(route_shape_id_relation[route_id].includes(shape_id))===false){
        route_shape_id_relation[route_id].push(shape_id);
      };
      if(headsign_shape_id_relation.hasOwnProperty(shape_id)===false){
        headsign_shape_id_relation[shape_id] = trip_headsign;
        //headsign_shape_id_relation[shape_id].push(trip_headsign);
      };
      //else if((headsign_shape_id_relation.hasOwnProperty(shape_id))
            //&&(route_shape_id_relation[route_id].includes(trip_headsign))===false){
        //route_shape_id_relation[route_id].push(trip_headsign);
      //};
  }
  }
  return {
    route_shape_id_relation,
    headsign_shape_id_relation
  }
}
function HandleStops(data){
  let stop_id = []
  let stop_name = []
  let stop_lat = []
  let stop_lon = []
  //let stops = []
  if(data.length !== 0){
    for (let i=0; i < data.length; i++){
      stop_id.push(data[i].stop_id);
      stop_name.push(data[i].stop_name);
      stop_lat.push(data[i].stop_lat);
      stop_lon.push(data[i].stop_lon);
    };
  };
  return {
    stop_id,
    stop_name,
    stop_lat,
    stop_lon
  };
}
function SetLabels(current_route, labelsConfig, stopsData, shapesData){
  shapesData.shape_pt_town=new Array(shapesData.shape_pt_lat.length).fill("");
  if((stopsData.stop_id.length !== 0)&&(typeof(labelsConfig.shape_id[current_route])!== 'undefined')){
    for (const [key, value] of Object.entries(labelsConfig.shape_id[current_route])) {
        for (let i=0; i < stopsData.stop_id.length; i++){
          if (stopsData.stop_id[i]==key){
              let lat_1 = stopsData.stop_lat[i]
              let lon_1 = stopsData.stop_lon[i]
              let dist = 1000000
              let index= null
              for(let j=0; j < shapesData.shape_pt_lat.length; j++){
                let lat_2=shapesData.shape_pt_lat[j]
                let lon_2=shapesData.shape_pt_lon[j]
                let haversine = Haversine(lat_1, lon_1, lat_2, lon_2)
                if (haversine<dist){
                  dist = haversine
                  index = j
                };
              };
            if(index!==null){
              shapesData.shape_pt_town[index]=value;
              };
          };
        };
    };
  }
  else{
    for (let i=0; i < stopsData.stop_id.length; i++){
      //if (stopsData.stop_id[i]==key){
          let lat_1 = stopsData.stop_lat[i]
          let lon_1 = stopsData.stop_lon[i]
          let dist = 1000000
          let index= null
          for(let j=0; j < shapesData.shape_pt_lat.length; j++){
            let lat_2=shapesData.shape_pt_lat[j]
            let lon_2=shapesData.shape_pt_lon[j]
            let haversine = Haversine(lat_1, lon_1, lat_2, lon_2)
            if (haversine<dist){
              dist = haversine
              index = j
            };
          };
          if((index!==null)){
            shapesData.shape_pt_town[index]=stopsData.stop_name[i];
          };
    };
  };
  return shapesData;
}
function SetLabel(current_route, tripsData, current_headsign=null){

  let label = null;
  //return label = tripsData.headsign_shape_id_relation[current_route]
  return label = current_headsign
}
function SetColor(current_route, tripsData, routesData){
  var hexColor=null
  var index = null
  var backgroundColor = null
  var borderColor = null
  //console.log(index)
  var route_id = () => {
    for (const [key, value] of Object.entries(tripsData)) {
      if(value.includes(current_route)){
        return key
      };
    };
  };
  if(routesData.route_id.includes(route_id())){
    index=routesData.route_id.indexOf(route_id())
    //console.log('holis1')
    //console.log(index)
    //console.log(routesData.route_id)
  };

  if(index!==-1 && index !==null){
    //console.log('holis2')
    //console.log(index)
    //console.log(routesData)
    hexColor = routesData.route_color[index]
    //console.log(hexColor)
  }
  else{
    //Add error when route_id has no relation to shape_id
    //console.log('shape_id has no route_id related value')
  };
  if (hexColor !== null){
    //console.log(hexColor)
    //console.log(Hex2Rgb(hexColor))
    backgroundColor = Hex2Rgb(hexColor)
    borderColor = Hex2Rgb(hexColor)
    backgroundColor.push(0.2)
    borderColor.push(1)
    backgroundColor='rgba('+backgroundColor.join()+')'
    borderColor='rgba('+borderColor.join()+')'
    //console.log(backgroundColor)
  }
  else{
    backgroundColor = 'rgba(255, 99, 132, 0.2)'
    borderColor = 'rgba(255, 99, 132, 1)'
  };
    //console.log(backgroundColor)
    return {
            backgroundColor,
            borderColor
           }
}
function Haversine(lat_start, lon_start, lat_sec, lon_sec){
  let dlat = lat_start - lat_sec
  let dlon = lon_start - lon_sec
  //console.log(lon_start, lon_sec)
  let a = Math.sin(dlat/2)**2 + Math.cos(lat_start) * Math.cos(lat_sec) * Math.sin(dlon/2)**2
  let c = 2 * Math.asin(Math.sqrt(a))
  let dist = 6367 * c
  return dist
}
function Hex2Rgb(color){
  //console.log(color)
  if(color.length !== 6){
        throw "Only six-digit hex colors are allowed.";
    }

    var aRgbHex = color.match(/.{1,2}/g);
    var aRgb = [
        parseInt(aRgbHex[0], 16),
        parseInt(aRgbHex[1], 16),
        parseInt(aRgbHex[2], 16)
    ];
    //console.log(aRgb)
    return aRgb;
}
function MovingAvg(array, count, qualifier){
    // calculate average for subarray
    var avg = function(array, qualifier){
        var sum = 0, count = 0, val;
        for (var i in array){
            val = array[i];
            if (!qualifier || qualifier(val)){
                ///console.log(count);
                sum += val;
                count++;
            }
        }
        return sum / count;
    };
    var result = [], val;
    // pad beginning of result with null values
    //for (var i=0; i < count-1; i++)
    //    result.push(null);
    // calculate average for each subarray and add to result
    for (var i=0, len=array.length - count; i <= len; i++){
        val = avg(array.slice(i, i + count), qualifier);
        if (isNaN(val)){
            result.push(null);
          }
        else{
            result.push(val);
          }
    }
    let filtered = result.filter(function(el){
      return el != null;
    });
    let missingPoints=result.length-filtered.length
    let index = (filtered.length/missingPoints)
    for (var i=0, len=missingPoints; i <= len; i++){
      filtered.splice(index*i, 0, null);
    }
    return filtered;
  }
