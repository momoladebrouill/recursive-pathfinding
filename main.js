let canvas = document.getElementById("fen");
let context = canvas.getContext("2d");
let W = window.innerWidth;
let H = window.innerHeight;
let ratio = window.devicePixelRatio;
canvas.width = W*ratio;
canvas.height = H*ratio;
canvas.style.width = W + "px";
canvas.style.height = H + "px";
context.scale(ratio,ratio);

let next_rockets=[];
let rockets=[];
let isdrawing=false;
let dict={};
let pos;

class Rocket{
	constructor(place){
		this.path=[]
		this.place=place
	}
}

document.addEventListener("keydown", keydown);
canvas.addEventListener("mousedown",mousedown);
canvas.addEventListener("mousemove",mousemove);
window.addEventListener("mouseup",mouseup);

function keydown(e){
	if (e.keyCode==32){
		if (pos){
			console.log(rockets)
			search()
		}else{
			console.log("pas de point de départ")
		}
	}
}

function mousedown(e){
	if(e.buttons==4){
		if (get_at(e)==2){
			set_at(e,3)
		}else if(get_at(e)==3){
			set_at(e,2)
		}else{
			set_at(e,2)
		}
		
	}else{
		if(get_at(e)==undefined){
			isdrawing="write"
		}else{
			isdrawing="delete"
		}
	}
	mousemove(e)	
}

function mouseup(e){isdrawing=false}

function mousemove(e){
	shell.textContent=[parseInt(e.offsetX/10),parseInt(e.offsetY/10)]
	if(isdrawing=="write"){
		set_at(e,1)
	}else if (isdrawing=="delete"){
		del_at(e)
	}
}

function get_at(e){return dict[[parseInt(e.offsetX/10),parseInt(e.offsetY/10)]]
}

function set_at(e,val){
	dict[[parseInt(e.offsetX/10),parseInt(e.offsetY/10)]]=val
	if (val==3){
		pos=[[parseInt(e.offsetX/10),parseInt(e.offsetY/10)]]
	}
}

function del_at(e) {delete dict[[parseInt(e.offsetX/10),parseInt(e.offsetY/10)]]}

function search() {
	if(rockets.length==0)
	{
		for(let i=0;i<8;i++){
			let gt=give_possible_go(pos)[i]
			append(gt,new Rocket(gt))
		}
	}
	else
	{
		for(ind in rockets)
		{
			rocket=rockets[ind]
			for(i=0;i<8;i++)
			{
				append(give_possible_go(rocket.place)[i],rocket)
			}
		}
	}
	rockets=[...next_rockets]
	for (var i = 0; i < rockets.length; i++) {
		dict[rockets[i]]=rockets[i]
	}
}

function append(place,fus) {
	if (dict[place]==undefined)
	{
		newbie=new Rocket(place)
		newbie.path=[...fus.path]
		next_rockets.push(newbie)
		dict[place]=newbie
	}
	else if(typeof dict[place]=="object")
	{
		if (dict[place].path.length>fus.path.length+1)
		{
			fus.path.push(place)
			dict[place]=fus
		}
	}
	else if(dict[place]==2)
	{
		console.log("hurray")
	}
}

function give_possible_go(place) {
	let ls=[]
	let cartesian=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
	for(i in cartesian)
	{
		goto=cartesian[i]
		ls.push([parseInt(place[0])+parseInt(goto[0]),
			parseInt(place[1])+parseInt(goto[1])])
	}
	return ls
} 

function bLoop() {
	
	context.beginPath()
	context.fillStyle='black'
	context.fillRect(0,0,W,H)
	context.fill()
	context.closePath()

	context.font = "50px cursive";
	context.fillStyle = "white";
	context.textBaseline = "middle"

	//context.fillText("jean",0,0)
	//shell.textContent=""
	for(key in dict){
		//shell.textContent+=key+" "
		key=key.split(',')
		if (typeof dict[key] == "number"){
			if(dict[key]==1){
				context.fillStyle="white"
			}else if(dict[key]==2){
				context.fillStyle="yellow"
			}else if(dict[key]==3){
				context.fillStyle="blue"
			}
		}else{
			context.fillStyle="lightblue"
		}
		context.fillRect(parseInt(key[0])*10,parseInt(key[1])*10,10,10)
	}
	requestAnimationFrame(bLoop)	
}

bLoop()