function lens(rad1, rad2, rad3, dist1,dist2,dist3)
    clc;
    num = 100;
    step = dist3 / num;
    x = [-dist3/2 : step : dist3/2];
    y = zeros(length(x),1);
    y0 = 0;
    y1 = 0;
    h1 = rad1 - 1/2 * sqrt(4 * rad1^2 - dist1^2);
    h2 = rad2 - 1/2 * sqrt(4 * rad2^2 - dist2^2);
    h3 = rad3 - 1/2 * sqrt(4 * rad3^2 - dist3^2);
    for k = 1 : length(x)
      if((x(k) < -dist2/2 )|| (x(k) > dist2/2))
        y0 = 0;
        y(k) =  sqrt(rad3.^2 - x(k).^2)+y0;
      elseif(x(k) < -dist1/2 || x(k) > dist1/2)
        y1 = sqrt(rad3^2 - (dist2/2)^2) - sqrt(rad2^2 - (dist2/2)^2) + y0;
        y(k) =  sqrt(rad2.^2-x(k).^2)+y1;
      elseif(x(k) > -dist1/2 || x(k) < dist1/2)
        y2 = y1  + sqrt(rad2^2 - (dist1/2)^2) - sqrt(rad1^2 - (dist1/2)^2);
        y(k) =  sqrt(rad1.^2-x(k).^2)+y2;
      endif
    endfor
    yt = y(1);
    for k = 1 : length(x)
      y(k) = y(k)-yt;
    endfor
    rad1
    rad2
    rad3
    dist1
    dist2
    dist3
    sag1 = h1
    sag2 = h2
    sag3 = h3
    plot(x,y);
    axis([(-dist3/2)-0.5 (dist3/2)+0.5 y(1)-dist3/2-0.5 y(1)+dist3/2+0.5]);
    grid minor;
    title("Lente de Perfil");
endfunction