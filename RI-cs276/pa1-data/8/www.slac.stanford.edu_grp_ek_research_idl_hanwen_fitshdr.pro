name fitshdr purpose extract display and write out the header of xte fits file s category xte calling sequence result fitshdr file optional inputs file name of the first xte fits file outputs this function returns the header of the last xte fits file opened optional outputs for each fits file opened a corresponding header file may be created containing the header information modification history written by han wen august 1996 function fitshdr file header 1 np n_params if np eq 1 then goto openfit path usr local ek xray_data xte select file pickfile path path title select fits file if file eq then goto quit openfit fxbopen lu file 1 header & n n_elements header fxbclose lu pos rstrpos file path strmid file 0 pos 1 name strmid file pos 1 10000 xmsg header title fits file name fout pickfile file path name+ hdr path path title select output fits header file if fout ne then begin openw lu fout get_lun for i 0 n 1 do printf lu header i free_lun lu endif goto select quit return header end
