args <- commandArgs(TRUE)
srcFile <- toString(args[1])
print(srcFile)

library(rtracklayer)

path = srcFile
bw_repl_tracks <- dir(path, pattern = "*.bw", full.names = TRUE)
bw_repl_track_names <- dir(path, pattern = "*.bw", full.names = F)

#bw_repl_tracks <- dir("~/../../mnt/d/Work/Stephan_IPSCS/rnaseq/bw_star", pattern = "*.bw", full.names = TRUE)
#bw_repl_track_names <- dir("~/../../mnt/d/Work/Stephan_IPSCS/rnaseq/bw_star", pattern = "*.bw", full.names = F)
new_folder = paste0(path,"/UCSC/")
dir.create(new_folder)

#samples <- substr(bw_repl_track_names,19,26)
samples <- bw_repl_track_names



for (i in 1:length(bw_repl_tracks)){
	  bwfile <- import.bw(bw_repl_tracks[i])
  seqlevelsStyle(bwfile) <- "UCSC"
    export.bw(bwfile,paste0(new_folder,samples[i]))
    print(samples[i])
      #export.bw(bwfile,paste0("atac/bw_merged/hg38/",samples[i],".bw"))
}

