import torch

def save_checkpoint(model, optimizer, epoch, loss, path:str):
    ckpt = {
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
        "epoch": epoch,
        "loss": loss
    }
    torch.save(ckpt, path)
    print(f"Checkpoint saved to {path}")

def load_checkpoint(model, optimizer, path:str, device):
    ckpt = torch.load(path, map_location=device)
    model.load_state_dict(ckpt["model_state_dict"])
    optimizer.load_state_dict(ckpt["optimizer_state_dict"])
    epoch = ckpt["epoch"]
    loss = ckpt["loss"]
    print(f"Loaded checkpoint epoch {epoch}, loss {loss:.4f}")
    return model, optimizer, epoch, loss
