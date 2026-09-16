(function(){var b=document.getElementById('tt-calc');if(!b)return;
function num(id){var e=document.getElementById(id);if(!e)return NaN;var v=parseFloat(e.value);return isNaN(v)?NaN:v;}
function out(){return document.getElementById('tt-out');}
function money(v){return v.toFixed(2).replace(/\.00$/,'').replace(/(\.\d)0$/,'$1');}
b.addEventListener('click',function(){
  var intro=num('tt-intro'),introm=Math.round(num('tt-introm')),renew=num('tt-renew'),
      keep=Math.round(num('tt-keep')),monthly=num('tt-monthly');
  if(!(intro>0&&intro<=2000)){out().textContent='Enter the introductory charge as a total (the lump sum the checkout page bills for the first term).';return;}
  if(!(introm>=1&&introm<=60)){out().textContent='Enter how many months the introductory charge covers (1-60), bonus months included.';return;}
  if(!(renew>=0&&renew<=2000)){out().textContent='Enter the renewal price per year, or 0 if the provider has none.';return;}
  if(!(keep>=1&&keep<=120)){out().textContent='Enter how many months you expect to keep the service (1-120).';return;}
  var after=Math.max(0,keep-introm);
  var renewcost=renew*after/12;
  var total=intro+renewcost;
  var eff=total/keep;
  var intro_m=intro/introm;
  var renew_m=renew/12;
  var lines=[];
  lines.push('Over '+keep+' months: about '+money(total)+' total = '+money(intro)+' up front + '+money(renewcost)+' of renewal'+(after>0?'':' (your horizon ends inside the intro term)')+'. Effective '+money(eff)+' per month.');
  if(renew>0&&intro_m>0){
    var jump=renew_m/intro_m;
    lines.push('Renewal jump: '+money(renew_m)+'/mo at renewal is '+jump.toFixed(1)+'x the '+money(intro_m)+'/mo introductory rate.');
  }else if(renew===0){
    lines.push('No renewal price entered, so the total above is the introductory charge spread over your horizon.');
  }
  if(monthly>0&&monthly<=200){
    var mcost=monthly*keep;
    var diff=mcost-total;
    lines.push('Month-to-month for '+keep+' months would cost '+money(mcost)+': the deal '+(diff>=0?'saves '+money(diff)+' over that horizon':'costs '+money(-diff)+' MORE than monthly over that horizon')+'.');
    var denom=monthly-renew_m;
    if(denom>0){
      var mbe=(intro-renew*introm/12)/denom;
      if(mbe>0){
        lines.push('Break-even: below about '+Math.max(1,Math.round(mbe))+' months of use, paying monthly is cheaper; beyond it, the introductory deal wins.');
      }
    }else{
      lines.push('With the renewal rate at or above the monthly price, the deal keeps winning for as long as you stay.');
    }
  }
  lines.push('Taxes, currency conversion and bank markups are excluded - a naira card paying a USD charge pays your bank\'s rate on the day too.');
  out().textContent=lines.join('\n');
});})();
